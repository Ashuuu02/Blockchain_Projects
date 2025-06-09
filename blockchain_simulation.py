import hashlib
import json
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash=""):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")
    
    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(
            index=prev_block.index + 1,
            timestamp=time.time(),
            data=data,
            previous_hash=prev_block.hash
        )
        self.chain.append(new_block)
    
    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            
            # Check hash integrity
            if current.hash != current.calculate_hash():
                return False
            
            # Check block linking
            if current.previous_hash != previous.hash:
                return False
        return True

# Create blockchain with 3 blocks
blockchain = Blockchain()
blockchain.add_block({"amount": 4})
blockchain.add_block({"amount": 8})

# Display blocks
print("BLOCKCHAIN VALID?:", blockchain.is_valid())
for block in blockchain.chain:
    print(f"\nBlock {block.index}:")
    print(f"Hash: {block.hash}")
    print(f"Prev Hash: {block.previous_hash}")
    print(f"Data: {block.data}")

# Tamper with Block 1
print("\n--- Tampering with Block 1 ---")
blockchain.chain[1].data = {"amount": 100}
print("BLOCKCHAIN VALID AFTER TAMPERING?:", blockchain.is_valid())