import sys
import csv
from tabulate import tabulate

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if not sys.argv[1].lower().endswith('.csv'):
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1]) as file:
        file = csv.DictReader(file)
        print(tabulate(file,header = "keys", tablefmt = "grid"))
except FileNotFoundError:
    sys.exit("File not found")
