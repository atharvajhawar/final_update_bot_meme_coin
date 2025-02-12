import json
import base58
from solders.keypair import Keypair
from solana.rpc.api import Client

# Load Private Key Securely
with open("config.json", "r") as f:
    config = json.load(f)

try:
    # Remove leading/trailing spaces from the private key
    private_key_base58 = config["private_key"].strip()

    # Decode the Base58 private key to bytes
    private_key_bytes = base58.b58decode(private_key_base58)

    # Ensure the private key is 64 bytes
    if len(private_key_bytes) != 64:
        raise ValueError("Invalid private key length. Expected 64 bytes.")

    # Load the keypair
    wallet = Keypair.from_bytes(private_key_bytes)
    public_address = str(wallet.pubkey())

    print(f"✅ Wallet Loaded! Public Address: {public_address}")

except Exception as e:
    print(f"❌ Error Loading Keypair: {e}")

# Solana RPC Client
SOLANA_RPC = "https://api.mainnet-beta.solana.com"
client = Client(SOLANA_RPC)
