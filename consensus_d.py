import random

# Mock Validators
miners = [
    {"id": "Miner A", "power": random.randint(1, 100)},
    {"id": "Miner B", "power": random.randint(1, 100)},
    {"id": "Miner C", "power": random.randint(1, 100)}
]

stakers = [
    {"id": "Staker X", "stake": random.randint(100, 1000)},
    {"id": "Staker Y", "stake": random.randint(100, 1000)},
    {"id": "Staker Z", "stake": random.randint(100, 1000)}
]

voters = ["Voter1", "Voter2", "Voter3"]
delegates = [
    {"id": "Delegate J", "votes": 0},
    {"id": "Delegate K", "votes": 0},
    {"id": "Delegate L", "votes": 0}
]

# Simulate PoW
def proof_of_work():
    selected = max(miners, key=lambda x: x["power"])
    print(f"\nPoW Selected: {selected['id']} (Power: {selected['power']})")
    print("Logic: Highest computational power wins")

# Simulate PoS
def proof_of_stake():
    selected = max(stakers, key=lambda x: x["stake"])
    print(f"\nPoS Selected: {selected['id']} (Stake: ${selected['stake']})")
    print("Logic: Highest staked amount wins")

# Simulate DPoS
def delegated_proof_of_stake():
    # Simulate voting
    for _ in range(len(voters)):
        delegate = random.choice(delegates)
        delegate["votes"] += 1
    
    selected = max(delegates, key=lambda x: x["votes"])
    print(f"\nDPoS Selected: {selected['id']} (Votes: {selected['votes']}/3)")
    print("Logic: Most votes from token holders")

# Run simulations
proof_of_work()
proof_of_stake()
delegated_proof_of_stake()