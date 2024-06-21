def main():
    fraction = convert(input("Fraction: "))
    print(gauge(fraction))



def convert(fraction):
    a,b = fraction.split("/")
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        raise ValueError
    if b == 0:
        raise ZeroDivisionError

    return round(a*100/b)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
