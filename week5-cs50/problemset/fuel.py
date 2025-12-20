def main():
    fraction = input("Fraction: ")
    print(gauge(convert(fraction)))


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x > y or x < 0 or y < 0:
            raise ValueError
        decimal = float(x / y)
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    
    return decimal * 100


def gauge(percentage):
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage:.0f}%")


if __name__ == "__main__":
    main()
