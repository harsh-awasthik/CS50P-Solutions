import sys

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if not sys.argv[1].endswith('.py'):
    sys.exit("Not a python file")

try:
    with open(sys.argv[1]) as file:
        l = 0
        for lines in file:
            line = lines.strip()
            if not line.startswith("#") and len(line) != 0:
                l += 1

except FileNotFoundError:
    sys.exit("File not found")

print(l)
