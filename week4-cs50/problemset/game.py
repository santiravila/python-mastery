import random


def main():
    while True:
        try:
            level = int(input("Level: ")) # where valueerror might happen
            if level < 1:
                continue
        except ValueError:
            pass
        else:
            answer = random.choice(range(1, level+1))
            while True:
                try:
                    guess = int(input("Guess: "))
                    if guess < 1:
                        continue
                except ValueError:
                    pass
                else:
                    if guess < answer:
                        print("Too small!")
                    elif guess > answer:
                        print("Too large!")
                    else:
                        print("Just right!")
                        return


main()