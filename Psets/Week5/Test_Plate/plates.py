def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            i = 0
            while i < len(s) and s[i].isalpha():
                i += 1
            if i != len(s):
                if s[i] != "0":
                    if s[i:].isnumeric():
                        return True
                return False
            return True
    return False


if __name__ == "__main__":
    main()
