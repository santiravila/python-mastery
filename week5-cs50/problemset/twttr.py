def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")


def shorten(word: str):
    for char in word.lower():
        if char in ['a', 'e', 'i', 'o', 'u']:
            word = word.replace(char, '') 


if __name__ == "__main__":
    main()