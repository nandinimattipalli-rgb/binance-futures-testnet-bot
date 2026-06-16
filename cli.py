<<<<<<< HEAD
import argparse
import logging
import os
import json
from datetime import datetime
from dotenv import load_dotenv
from binance.um_futures import UMFutures

# --- Logging Setup ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

# --- Load ENV ---
load_dotenv()
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# --- CLI Args ---
parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
parser.add_argument("--symbol",   required=True,  help="Trading pair e.g. BTCUSDT")
parser.add_argument("--side",     required=True,  choices=["BUY", "SELL"])
parser.add_argument("--type",     required=True,  choices=["MARKET", "LIMIT"])
parser.add_argument("--quantity", required=True,  type=float)
parser.add_argument("--price",    required=False, type=float, help="Required for LIMIT orders")
parser.add_argument("--mock",     action="store_true", help="Run without placing real order")
args = parser.parse_args()

# --- Validation ---
if args.type == "LIMIT" and not args.price:
    logger.error("--price is required for LIMIT orders")
    exit(1)

# --- Mock Mode ---
if args.mock:
    logger.info("MOCK MODE — no real order placed")
    mock_order = {
        "orderId": 123456789,
        "symbol": args.symbol,
        "side": args.side,
        "type": args.type,
        "quantity": args.quantity,
        "price": args.price or "MARKET",
        "status": "FILLED (mock)",
        "timestamp": datetime.now().isoformat()
    }
    logger.info("Mock Order Result:\n" + json.dumps(mock_order, indent=2))
    exit(0)

# --- Real Order ---
try:
    client = UMFutures(key=API_KEY, secret=API_SECRET, base_url="https://testnet.binancefuture.com")
    logger.info(f"Placing {args.type} {args.side} order for {args.quantity} {args.symbol}...")

    params = {
        "symbol": args.symbol,
        "side": args.side,
        "type": args.type,
        "quantity": args.quantity,
    }
    if args.type == "LIMIT":
        params["price"] = args.price
        params["timeInForce"] = "GTC"

    order = client.new_order(**params)

    logger.info("ORDER PLACED SUCCESSFULLY")
    logger.info(f"Order ID : {order['orderId']}")
    logger.info(f"Status   : {order['status']}")
    logger.info(f"Symbol   : {order['symbol']}")
    logger.info(f"Side     : {order['side']}")
    logger.info(f"Type     : {order['type']}")
    logger.info(f"Quantity : {order['origQty']}")

except Exception as e:
    logger.error(f"ORDER FAILED: {e}")
    exit(1)
=======
from dotenv import load_dotenv
from binance.client import Client
import os

load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

client = Client(api_key, api_secret)
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

try:
    order = client.futures_create_order(
        symbol="BTCUSDT",
        side="BUY",
        type="LIMIT",
        quantity=0.001,
        price="50000",
        timeInForce="GTC"
    )

    print("LIMIT ORDER SUCCESS")
    print("Order ID:", order["orderId"])
    print("Status:", order["status"])

except Exception as e:
    print("ORDER FAILED")
    print(e)
>>>>>>> e0eda05680ed9784cbf40fb1af540affb609656f
