import sys
import csv


if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if not sys.argv[1].lower().endswith('.csv') and sys.argv[2].lower().endswith('.csv'):
    sys.exit("Not a CSV file")

with open(sys.argv[1], 'r') as input, open(sys.argv[2], 'w') as output:
    input = csv.DictReader(input)
    headers = ["first","last", "house"]
    output = csv.DictWriter(output, fieldnames = headers)
    output.writeheader()

    for line in input:
        name = line["name"].split(",")
        output.writerow({"first": name[1].strip(), "last": name[0].strip(), "house": line["house"].strip()})
