from PIL import Image, ImageOps
import sys


images = []

if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
else:
    try:
        formats=["png","jpg","jpeg"]
        if sys.argv[2].split(".")[1] in formats:
            if sys.argv[1].split(".")[1]==sys.argv[2].split(".")[1]:
                image=Image.open(sys.argv[1])
                shirt=Image.open("shirt.png")
                size=shirt.size
                muppet=ImageOps.fit(image,size)
                muppet.paste(shirt, shirt)
                muppet.save(sys.argv[2])


            else:
                sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid output")
    except FileNotFoundError:
        sys.exit("Input does not exist")
