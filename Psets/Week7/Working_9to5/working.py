import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time = re.search(r"([0-9]{1,2}):?([0-9]{2})? (AM|PM) to ([0-9]{1,2}):?([0-9]{2})? (AM|PM)", s)


    if not time:
        raise ValueError

    inhrs,outhrs = int(time.group(1)), int(time.group(4))

    if time.group(2):
        inmin = int(time.group(2))
    else:
        inmin = 00

    if time.group(5):
        outmin = int(time.group(5))
    else:
        outmin = 00

    if (inhrs > 12 or
        outhrs > 12 or
        inmin > 59 or
        outmin > 59):
        raise ValueError


    if time.group(3) == "PM" and inhrs != 12:
        inhrs += 12
    elif time.group(3) == "AM" and inhrs == 12:
        inhrs = 00

    if time.group(6) == "PM" and outhrs != 12:
        outhrs += 12
    elif time.group(6) == "AM" and outhrs == 12:
        outhrs = 00

    return f"{inhrs :02}:{inmin :02} to {outhrs :02}:{outmin :02}"

...


if __name__ == "__main__":
    main()
