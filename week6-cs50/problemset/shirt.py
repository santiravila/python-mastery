import sys
from PIL import Image, ImageOps

def main():
    error_message = validate_cla(sys.argv)
    if error_message:
        sys.exit(error_message)

    infilename = sys.argv[1]
    outfilename = sys.argv[2]
    try:
        overlay_image(infilename, outfilename)
    except FileNotFoundError:
        sys.exit("Input does not exist")


def overlay_image(infilename, outfilename):
    with Image.open(infilename, "r") as before, Image.open("shirt.png", "r") as shirt:
        fitted_before = ImageOps.fit(before, shirt.size)

        fitted_before.paste(shirt, shirt)
        
        fitted_before.save(outfilename) 


def validate_cla(arguments: list) -> str | None:
    if len(arguments) < 3:
        return "Too few command-line arguments"
    elif len(arguments) > 3:
        return "Too many command-line arguments"
    elif not arguments[1].endswith((".jpg", ".jpeg", ".png")):
        return "Invalid Input"
    else:
        extension1 = sys.argv[1].split(".")[-1]
        extension2 = sys.argv[2].split(".")[-1]
        if extension1 != extension2:
            return "Input and output have different extensions"
    
    return None


main()