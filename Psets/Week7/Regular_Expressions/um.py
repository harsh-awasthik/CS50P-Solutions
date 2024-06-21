import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = re.findall(r"\bum\b", s, flags=re.IGNORECASE)
    return len(count)



...


if __name__ == "__main__":
    main()
