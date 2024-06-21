from datetime import date
import sys
import inflect

p = inflect.engine()



def main():
    print(time_to_dob(input("Date of Birth: ")))

def time_to_dob(dob):
    d = date.today()
    dob = dob.split("-")
    try:
        dob = date(int(dob[0]), int(dob[1]), int(dob[2]))
    except ValueError:
        sys.exit("Enter Correct DOB")

    minutes = abs(d - dob).days * 24 * 60
    words = p.number_to_words(minutes, andword = "").capitalize()
    return words + " minutes"


if __name__ == "__main__":
    main()
