import time
import requests

# ✅ Correct DexScreener API for Solana
DEXSCREENER_API = "https://api.dexscreener.com/latest/dex/search/?q=SOL"

# Trading Filters
MIN_LIQUIDITY = 10000  # Lowered from 100K to 10K
MIN_BUYS = 5           # Lowered from 50 to 5 for testing
BUY_AGE_LIMIT = 4 * 60  # Increased from 4 to 10 minutes

def fetch_new_meme_coins():
    """Fetches new meme coins from DexScreener API and filters them."""
    try:
        response = requests.get(DEXSCREENER_API, timeout=10)
        response.raise_for_status()  # Ensure successful response

        data = response.json()
        if "pairs" not in data:
            print("❌ API Response Error: 'pairs' key missing")
            return []

    except requests.exceptions.RequestException as e:
        print(f"❌ API Request Failed: {e}")
        return []

    eligible_coins = []
    current_time = time.time()

    for pair in data.get("pairs", []):
        try:
            # Convert timestamp to seconds and calculate age
            pair_age = current_time - (pair["pairCreatedAt"] / 1000)

            # Extract liquidity and buy transactions
            liquidity = pair.get("liquidity", {}).get("usd", 0)
            buys_24h = pair.get("txns", {}).get("h24", {}).get("buys", 0)

            print(f"🔍 {pair['baseToken']['symbol']}: Liquidity ${liquidity}, Buys {buys_24h}, Age {pair_age:.2f}s")

            if liquidity >= MIN_LIQUIDITY and buys_24h >= MIN_BUYS and 0 < pair_age < BUY_AGE_LIMIT:
                eligible_coins.append({
                    "pair": pair["pairAddress"],
                    "token_name": pair["baseToken"]["name"],
                    "token_symbol": pair["baseToken"]["symbol"],
                    "liquidity": liquidity,
                    "buys_24h": buys_24h,
                    "age_seconds": pair_age
                })

        except KeyError as e:
            print(f"⚠️ Skipping a pair due to missing key: {e}")

    return eligible_coins


new_coins = fetch_new_meme_coins()

if new_coins:
    print(f"✅ Found {len(new_coins)} eligible new meme coins!")
    for coin in new_coins:
        print(f"🪙 {coin['token_symbol']} ({coin['token_name']}): Liquidity: ${coin['liquidity']}, Buys: {coin['buys_24h']}, Age: {coin['age_seconds']}s")
else:
    print("❌ No eligible coins found.")
