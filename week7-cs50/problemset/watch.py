import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'^<iframe.*?src="https?:\/\/(?:www\.)?(?P<URL>youtube\.com\/embed\/\w+)" ?.*><\/iframe>$'
    if match := re.search(pattern, s):
        return "https://" + match.group("URL").replace("youtube.com/embed", "youtu.be")
    else:
        return None

if __name__ == "__main__":
    main()
