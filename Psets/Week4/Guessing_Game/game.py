from random import randint
import sys


def main():
    lvl = get_int("Level: ")
    i = randint(1, lvl)
    guess = 0
    while guess != i:
        guess = get_int("Guess: ")
        if guess > i:
            print("Too large!")
        elif guess < i:
            print("Too small!")
        else:
            print("Just right!")
    sys.exit()


def get_int(promt):
    value = 0
    while value <= 0:
        try:
            value = int(input(promt))
        except ValueError:
            pass
    return value


main()
