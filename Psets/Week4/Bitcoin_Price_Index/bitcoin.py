import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line arguments")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

bitcoin = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
bitcoin = bitcoin.json()['bpi']
USDrate = bitcoin["USD"]["rate_float"]

print(f"${n*USDrate:,.4f}")

