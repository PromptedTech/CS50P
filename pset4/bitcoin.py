import requests
import sys

try:
    num = float(sys.argv[1])
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=99a8d8757d47e41bf0558bd93db666149d19fdb3fd0586e6c2c480a8309a8eee")
    data = response.json()
    price = float(data['data']['priceUsd'])
    print(f"${num * price:,.4f}")
except ValueError:
    sys.exit('Invalid number of bitcoin')
except requests.RequestException:
    sys.exit('theres some problem with the API')