import sys
from PIL import Image, ImageOps

if len(sys.argv) > 3:
    sys.exit("Too-many command line arguments.")
elif len(sys.argv) < 3:
    sys.exit("Too-few command line arguments.")

input = sys.argv[1]
output = sys.argv[2]
if (input.split(".")[-1].lower() not in ["jpg","png","jpeg"]) or (output.split(".")[-1].lower() not in ["jpg","png","jpeg"]):

    sys.exit("Invalid Input")

if input.split(".")[-1].lower() != output.split(".")[-1].lower():
    sys.exit("Input and Output have different extensions")

try:
    image = Image.open(input)
    shirt = Image.open("shirt.png")
except FileNotFoundError:
    sys.exit("Input does not exist")

image = ImageOps.fit(image,shirt.size)

image.paste(shirt, mask = shirt)
image.save(output)

