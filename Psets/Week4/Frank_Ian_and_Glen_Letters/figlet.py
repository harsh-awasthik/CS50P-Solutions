from pyfiglet import Figlet
from random import choice
import sys
figlet = Figlet()

if len(sys.argv) == 2 or len(sys.argv) > 3:
    sys.exit("Invalid Usage")

elif len(sys.argv) == 1:
    figlet.setFont(font=choice(figlet.getFonts()))
    print(figlet.renderText(input("Input: ")))


else:
    if sys.argv[1] in ["-f", "--font"]:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(input("Input: ")))
    else:
        sys.exit("Invalid Usage")

