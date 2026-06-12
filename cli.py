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