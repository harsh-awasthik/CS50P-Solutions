def main():
    inp = input("Input: ")
    print(shorten(inp))


def shorten(word):
    for a in word:
        if a in "aeiouAEIOU":
            word = word.replace(a, "")
    return word

if __name__ == "__main__":
    main()
