VOWELS = ['a', 'e', 'i', 'o', 'u']

word = input("Input: ")

for letter in word:
    if letter.lower() in VOWELS:
        word = word.replace(letter, "")

print(f"Output: {word}")