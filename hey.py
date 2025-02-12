import requests

DEXSCREENER_API = "https://api.dexscreener.com/latest/dex/pairs/solana"

response = requests.get(DEXSCREENER_API)
if response.status_code == 200:
    data = response.json()
    print("✅ API Response Sample:")
    print(data)  # Print the full JSON structure
else:
    print(f"❌ API Error: {response.status_code}")