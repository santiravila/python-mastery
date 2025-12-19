import requests
import sys


URL = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=af9bd0a98cf97d4da1a536efdb557b2a2d428a2eb6e42ffbc4fedb7d2410b57a"

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoin_number = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    try:
        response = requests.get(URL)
        bitcoin_price = float(response.json()["data"]["priceUsd"])
        result = bitcoin_number * bitcoin_price
        print(f"${result:,.4f}")
    except requests.RequestException:
        pass   


main()