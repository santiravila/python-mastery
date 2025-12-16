def main():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if x > y or x < 0 or y < 0:
                continue
            decimal = float(x / y)
            break
        except ZeroDivisionError:
            pass
        except ValueError:
            pass    
        
    percentage = decimal * 100
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage:.0f}%")


main()