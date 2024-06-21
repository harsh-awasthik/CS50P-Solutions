l = []
while True:
    try:
        item = input()
        l.append(item.upper())
    except(EOFError):
        break

l.sort()
d = {}

for a in l:
    if a in d:
        d[a] += 1
    else:
        d[a] = 1

for a in d:
    print(d[a],a)
