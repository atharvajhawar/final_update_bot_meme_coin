from solders.keypair import Keypair
import json
import base58

# Generate a new Solana wallet
wallet = Keypair()
private_key = base58.b58encode(wallet.secret()).decode("utf-8")
public_key = str(wallet.pubkey())

# Save to config.json
config = {
    "private_key": private_key,
    "public_key": public_key
}

with open("config.json", "w") as f:
    json.dump(config, f, indent=4)

print(f"✅ Private Key saved to config.json")
print(f"🪙 Your Public Address: {public_key}")