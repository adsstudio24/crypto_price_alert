import requests
import time

API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

def check_price():
    response = requests.get(API_URL).json()
    price = response["bitcoin"]["usd"]
    print(f"📈 Поточна ціна BTC: ${price}")

while True:
    check_price()
    time.sleep(60)
