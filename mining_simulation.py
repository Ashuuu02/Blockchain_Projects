import hashlib
import json
import time

class Block:
    def __init__(self, index, data, previous_hash=""):
        self.index = index
        self.timestamp = time.time()
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
    
    def mine_block(self, difficulty):
        start_time = time.time()
        target = "0" * difficulty
        
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        
        time_taken = time.time() - start_time
        print(f"Block mined with nonce {self.nonce} in {time_taken:.4f} seconds")
        print(f"Final Hash: {self.hash}")

# Mine a block with difficulty 4
print("Mining block with difficulty 4...")
block = Block(1, {"amount": 5})
block.mine_block(4)

# Mine with higher difficulty (notice increased time)
print("\nMining block with difficulty 5...")
harder_block = Block(2, {"amount": 10})
harder_block.mine_block(5)