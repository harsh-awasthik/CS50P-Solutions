import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ipa =  re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)
    if ipa:
        if int(ipa.group(1)) <= 255 and int(ipa.group(2)) <= 255 and int(ipa.group(3)) <= 255 and int(ipa.group(4)) <= 255:
            return True
    return False

if __name__ == "__main__":
    main()
