import random


def main():
    level = get_level()
    total_score = 0

    # generate random x,y pairs 10 times
    for _ in range(10):
        remaining_attempts = 3
        pair = (generate_integer(level), generate_integer(level))
        x = int(pair[0])
        y = int(pair[1])
        while remaining_attempts > 0:
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                remaining_attempts -= 1
                print("EEE")
                pass
            else:
                if answer == x + y:
                    total_score += 1
                    break
                else:
                    remaining_attempts -= 1
                    print("EEE")
                    continue

        if remaining_attempts == 0:
            print(f"{x} + {y} = {x + y}")
    print(f"Score: {total_score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                continue
        except ValueError:
            pass
        else:
            return level


# randomly generate and return a 'level' number of digits positive integer
def generate_integer(level):
    if level == 1:
        return random.choice(range(0, 10))
    elif level == 2:
        return random.choice(range(10, 100))
    elif level == 3:
        return random.choice(range(100, 1000))


if __name__ == "__main__":
    main()