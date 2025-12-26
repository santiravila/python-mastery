import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^([\d]{1,3})\.([\d]{1,3})\.([\d]{1,3})\.([\d]{1,3})$"
    if match := re.search(pattern, ip):
        numbers = list(match.groups())
        for number in numbers:
            if len(number) > 1 and number[0] == '0':
                return False
            if int(number) < 0 or int(number) > 255:
                return False
        return True

    return False


if __name__ == "__main__":
    main()
