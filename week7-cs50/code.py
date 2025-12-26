import re


def main():
    code = input("Hexadecimal color code: ")
    
    pattern = r"^#[0-9A-F]{6}$"
    match = re.search(pattern, code, re.IGNORECASE)
    if match:
        print(f"Valid. Matched with {match.group()}")
    else:
        print("Invalid.")

main()