def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str):
    return plate_length(s) and letter_number(s) and number_position(s) and punctuation(s)


def plate_length(s: str):
    return 2 <= len(s) <= 6


def letter_number(s: str):
    return s[:2].isalpha()


def number_position(s: str):
    for char in s:
        if char.isdigit():
            if char == "0":
                return False
           
            numbers = s.split(char, maxsplit=1)[1]
            for num in numbers:
                if num.isalpha():
                    return False
            return True
    return True


def punctuation(s: str):
    for character in s:
        if not character.isalpha() and not character.isdigit():
            return False
    return True


main()