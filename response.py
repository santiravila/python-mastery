import validators


def main():
    print(validate(input("What's your email address? ").strip()))


def validate(s):
    return "Valid" if validators.email(s) else "Invalid"


main()
