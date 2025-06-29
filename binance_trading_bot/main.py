import argparse
import logging
from config import API_KEY, API_SECRET
from bot import BasicBot

logging.basicConfig(filename="logs/bot.log", level=logging.INFO)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("order_type", choices=["market", "limit"])
    parser.add_argument("side", choices=["buy", "sell"])
    parser.add_argument("symbol", help="e.g., BTCUSDT")
    parser.add_argument("quantity", type=float)
    parser.add_argument("--price", type=float, help="Required for limit orders")

    args = parser.parse_args()
    bot = BasicBot(API_KEY, API_SECRET)

    if args.order_type == "market":
        bot.place_market_order(args.symbol.upper(), args.side, args.quantity)
    elif args.order_type == "limit":
        if not args.price:
            print("Price is required for limit orders.")
        else:
            bot.place_limit_order(args.symbol.upper(), args.side, args.quantity, args.price)

if __name__ == "__main__":
    main()
