import time
from dexscreener_fetch import fetch_new_meme_coins
from trade_executor import execute_trade

SELL_AGE_LIMIT = 4.5 * 60  # Sell at 4 minutes 30 seconds

def main():

    while True:
        meme_coins = fetch_new_meme_coins()
        for coin in meme_coins:
            execute_trade(coin["pairAddress"], trade_type="buy")
            time.sleep(SELL_AGE_LIMIT - 4 * 60)  # Wait until sell time
            execute_trade(coin["pairAddress"], trade_type="sell")

        time.sleep(10)

if __name__ == "__main__":
    main()
