import sys
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from utf8_converter import utf8_hex_representation

def create_op_return_tx(message, sat_amount, utxo_inputs, destinations):
    # Convert message to hex using your utf8_hex_representation function
    op_return_data = utf8_hex_representation(message)

    # Connect to Bitcoin Core
    rpc_user = "your_rpc_user"
    rpc_password = "your_rpc_password"
    rpc_host = "127.0.0.1"
    rpc_port = "8332"

    rpc_url = f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}"
    rpc_connection = AuthServiceProxy(rpc_url)

    try:
        # Create a raw transaction with OP_RETURN output
        tx_ins = [{"txid": utxo["txid"], "vout": utxo["vout"]} for utxo in utxo_inputs]
        tx_outs = {dest["address"]: dest["amount"] for dest in destinations}
        tx_outs["data"] = op_return_data  # OP_RETURN data

        raw_tx = rpc_connection.createrawtransaction(tx_ins, tx_outs)
        funded_tx = rpc_connection.fundrawtransaction(raw_tx)
        signed_tx = rpc_connection.signrawtransactionwithwallet(funded_tx["hex"])

        # Check if the transaction is fully signed
        if not signed_tx["complete"]:
            print("Transaction not fully signed.")
            sys.exit(1)

        # Broadcast the transaction
        txid = rpc_connection.sendrawtransaction(signed_tx["hex"])

        print("Transaction broadcasted successfully.")
        print(f"Transaction ID: {txid}")

    except JSONRPCException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def main():
    message = input("Enter the OP_RETURN message: ")

    sat_amount = int(input("Enter the amount of satoshis to send: "))

    # Input UTXO details
    utxo_inputs = []
    while True:
        txid = input("Enter UTXO txid (or press enter to finish): ")
        if not txid:
            break
        vout = int(input("Enter UTXO vout: "))
        utxo_inputs.append({"txid": txid, "vout": vout})

    # Input destination details
    destinations = []
    while True:
        address = input("Enter destination address (or press enter to finish): ")
        if not address:
            break
        amount = float(input("Enter amount in BTC to send to this address: "))
        destinations.append({"address": address, "amount": amount})

    create_op_return_tx(message, sat_amount, utxo_inputs, destinations)

if __name__ == "__main__":
    main()
