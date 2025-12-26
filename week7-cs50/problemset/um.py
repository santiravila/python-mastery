import re


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\b(um)\b"
    if match := re.findall(pattern, s, re.IGNORECASE):
        return len(match)
    else:
        return 0


if __name__ == "__main__":
    main()

