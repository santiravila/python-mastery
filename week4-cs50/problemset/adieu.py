import inflect


def main():
    p = inflect.engine()
    name_list = []
    while True:
        try:
            name = input("Name: ")
        except EOFError:
            print()
            print(f"Adieu, adieu, to {p.join(name_list)}")
            break 
        else:
            name_list.append(name)

main()