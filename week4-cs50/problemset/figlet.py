import sys
import random
import pyfiglet


FONTS = pyfiglet.FigletFont.getFonts()

def main():
    if len(sys.argv) == 1:
        text = input("Input: ")

        # output text with a random font
        random_font = random.choice(FONTS)
        new_text = pyfiglet.figlet_format(text, font=random_font)
        print(f"Output: {new_text}")
    elif len(sys.argv) == 3:
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (sys.argv[2] in FONTS):
            text = input("Input: ")
            new_text = pyfiglet.figlet_format(text, font=sys.argv[2])
            print(f"Output: {new_text}")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")



main()