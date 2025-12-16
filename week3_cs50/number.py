def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt: str):
    while True:
        try: 
            return int(input(prompt))
        except ValueError:
            pass