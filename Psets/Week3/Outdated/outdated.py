l = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip().split(" ")
        date[0] = l.index(date[0].title()) + 1
        if date[1][-1] == ",":
            date[1] = date[1][:-1]
        else:
            continue
        date[1] = int(date[1])
        date[2] = int(date[2])
        if 0 < date[1] < 31:
            break

    except (ValueError, IndexError):
        try:
            date = date[0].strip().split("/")
            for i in range(3):
                date[i] = int(date[i])
            if 0 < date[1] < 32 and 0 < date[0] < 13:
                break

        except (ValueError, IndexError):
            pass


print(f"{date[2]:04}-{date[0]:02}-{date[1]:02}")
