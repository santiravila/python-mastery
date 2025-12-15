"""
for each letter, determine whether is upper case. If so, replace with _ followed by lowercase letter
"""

word = input("camelCase: ")

for letter in word:
    if letter.isupper():
        word = word.replace(letter, f"_{letter.lower()}")

print(f"snake_case: {word}")