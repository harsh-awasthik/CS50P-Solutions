inp = input("Input: ")
for a in inp:
    if a in "aeiouAEIOU":
        inp = inp.replace(a, "")
print("Output:", inp)
