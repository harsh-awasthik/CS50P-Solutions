import inflect
p = inflect.engine()

l = []

while True:
    try:
        name = input("Name: ").strip()
    except EOFError:
        break
    else:
        l.append(name)

print()
for i in range(1, len(l)+1):
    print(f"Adieu, adieu, to {p.join(l[:i])}")

