from random import randint


def main():
    lvl = get_level()

    score = 0
    for i in range(10):
        x = generate_integer(lvl)
        y = generate_integer(lvl)

        correct = False
        tries = 0
        while not correct and tries < 3:
            print(f"{x} + {y} = ", end = "")

            try:
                ans = int(input())
            except ValueError:
                ans = 0

            if ans == x+y:
                correct = True

            else:
                print("EEE")
                tries += 1
        if correct:
            score += 1
        if tries == 3:
            print(f"{x} + {y} = {x+y}")
    print("Score:", score)


def get_level():
    lvl = 0
    while lvl not in [1,2,3]:
        try:
            lvl = int(input("Level: "))
        except ValueError:
            pass
    return lvl


def generate_integer(level):
    if level == 1:
        return randint(0,9)
    elif level == 2:
        return randint(10,99)
    elif level == 3:
        return randint(100,999)
    return ValueError


if __name__ == "__main__":
    main()
