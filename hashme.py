import hashlib

def bitcoin_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def mine_block(data, leading_zeros):
    nonce = 0
    while True:
        block_header = data + str(nonce)
        first_hash = bitcoin_hash(block_header)
        second_hash = bitcoin_hash(first_hash)
        print(f"Hashing {block_header}: {first_hash} -> {second_hash}")
        if second_hash.startswith('0' * leading_zeros):
            return second_hash, nonce
        nonce += 1

if __name__ == "__main__":
    data = input("Enter the data to hash: ")
    leading_zeros = int(input("Enter the number of leading zeros desired: "))
    hashed_result, nonce = mine_block(data, leading_zeros)
    print("Hashed result:", hashed_result)
    print("Nonce:", nonce)
