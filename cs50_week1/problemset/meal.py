def main():
    time = input("What time is it? ").strip()
    hour = convert(time)
    if 7 <= hour <= 8:
        print("breakfast time")
    elif 12 <= hour <= 13:
        print("lunch time")
    elif 18 <= hour <= 19:
        print("dinner time")


def convert(time):
    hour = int(time.split(':')[0])
    if ' ' in time:
        period = time.split(' ')[1]

        if period == 'a.m.':
            if hour == 12:
                hour = 0
            time = time.replace(' a.m.', '')

        elif period == 'p.m.':
            time = time.replace(' p.m.', '')
            if hour < 12:
                minutes = time.split(':')[1]
                hour += 12
                minutes = int(minutes) / 60
                return hour + minutes

    minutes = time.split(':')[1]
    minutes = int(minutes) / 60

    return hour + minutes


if __name__ == "__main__":
    main()

