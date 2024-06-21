import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    add = re.search(r"^<iframe.+https?://(?:www\.)?youtube\.com/embed/(.{11}).+</iframe>", s)

    if add:
        return "https://youtu.be/" + add.group(1)

    return None


if __name__ == "__main__":
    main()
