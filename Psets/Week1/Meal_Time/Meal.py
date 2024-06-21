def main():
    t = input("What time is it? ")
    t = convert(t)
    if t >= 7 and t <= 8:
        print("breakfast time")
    elif t >= 12 and t <= 13:
        print("lunch time")
    elif t >= 18 and t <= 19:
        print("dinner time")


def convert(time):
    h, m = time.split(":")
    m = int(m)/60
    return float(h) + m


if __name__ == "__main__":
    main()
