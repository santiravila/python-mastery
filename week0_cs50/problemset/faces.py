"""
Replace smiling and frowning with their respective emojis
"""


def main() -> None:
    text = input()
    print(convert(text))


def convert(text: str) -> str:
    return text.replace(':)', '🙂').replace(':(', '🙁')


main()
