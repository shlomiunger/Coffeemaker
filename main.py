import sys
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from utf8_converter import utf8_hex_representation


# Connect to Bitcoin Core
def connect_to_rpc():
    rpc_user = "shlomi"
    rpc_password = "768841"
    rpc_host = "127.0.0.1"
    rpc_port = "8332"

    rpc_url = f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}"
    return AuthServiceProxy(rpc_url)


def create_op_return_tx(rpc_connection, hex_message, utxo_inputs, destinations):
    # Set OP_RETURN variable to be equal to hex_message generated in main() function
    op_return_data = hex_message

    try:
        # Create a raw transaction with OP_RETURN output
        tx_ins = [{"txid": utxo["txid"], "vout": utxo["vout"]} for utxo in utxo_inputs]
        tx_outs = {dest["address"]: dest["amount"] for dest in destinations}
        tx_outs["data"] = op_return_data  # OP_RETURN data

        raw_tx = rpc_connection.createrawtransaction(tx_ins, tx_outs)
        funded_tx = rpc_connection.fundrawtransaction(raw_tx)

        # Prompt user to sign the transaction
        sign_tx = input("Do you want to sign this transaction? (y/n): ")
        if sign_tx.lower() == 'y':
            signed_tx = rpc_connection.signrawtransactionwithwallet(funded_tx["hex"])
            if not signed_tx["complete"]:
                print("Transaction not fully signed.")
                sys.exit(1)
            signed_tx_hex = signed_tx["hex"]
            print("Transaction signed successfully.")

            # Prompt user to send the transaction
            send_tx = input("Do you want to send this transaction? (y/n): ")
            if send_tx.lower() == 'y':
                txid = rpc_connection.sendrawtransaction(signed_tx_hex)
                print("Transaction broadcasted successfully.")
                print(f"Transaction ID: {txid}")
            else:
                print("Transaction not sent.")
        else:
            print("Transaction not signed.")

    except JSONRPCException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


def list_utxos(rpc_connection):
    try:
        utxos = rpc_connection.listunspent()
        return utxos
    except JSONRPCException as e:
        print(f"Error listing UTXOs: {e}")
        return []


def main():
    message = input("Enter the OP_RETURN message: ")

    # Check if message exceeds 80 bytes
    hex_message = utf8_hex_representation(message)
    num_bytes = len(hex_message) // 2
    if num_bytes > 80:
        print("Error: OP_RETURN message cannot exceed 80 bytes.")
        sys.exit(1)

    # Connect to Bitcoin Core
    rpc_connection = connect_to_rpc()

    # Retrieve UTXO inputs from Bitcoin Core
    utxo_inputs = list_utxos(rpc_connection)

    # Input destination details
    destinations = []
    while True:
        address = input("Enter destination address (or press enter to finish): ")
        if not address:
            break
        amount = input("Enter amount in BTC to send to this address: ")
        destinations.append({"address": address, "amount": amount})

    # Create the transaction
    create_op_return_tx(rpc_connection, hex_message, utxo_inputs, destinations)


if __name__ == "__main__":
    main()
