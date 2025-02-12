from solana.transaction import Transaction
from solana.rpc.types import TxOpts
from solana.rpc.commitment import Confirmed
from solana_utils import client, wallet

def execute_trade(pair_address, trade_type="buy"):
    """Executes buy/sell order on Solana DEX (Raydium or Jupiter)."""
    print(f"🔄 {trade_type.capitalize()} order for {pair_address}")

    # Example transaction (Replace with real transaction logic)
    transaction = Transaction()
    transaction.sign(wallet)  # Sign with private key

    # Send transaction to blockchain
    response = client.send_transaction(transaction, wallet, opts=TxOpts(preflight_commitment=Confirmed))

    if "result" in response:
        print(f"✅ {trade_type.capitalize()} successful: {response['result']}")
    else:
        print(f"❌ {trade_type.capitalize()} failed: {response}")
