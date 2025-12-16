def main() -> None:
    x = int(input("What's x? "))
    result = "Even" if is_even(x) else "Odd"
    print(result) 


def is_even(n: int) -> bool:
    return n % 2 == 0


main()

