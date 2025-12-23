def main():
    read_from_file()
    #name = input("What's your name? ")

#file = open("names.txt", "a")
def write_to_file(name):
    with open("names.txt", "a") as file:
        file.write(f"{name}\n")

def read_from_file():
    names = []
    with open("names.txt") as file:
        for line in file:
            names.append(line.rstrip())
    for name in sorted(names):
        print("hello", name)
#file.close()

if __name__ == "__main__":
    main()