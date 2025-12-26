import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # VALIDATION
    pattern = r'(?P<H1>\d{1,2}):?(?P<M1>\d{1,2})? (?P<P1>AM|PM) to (?P<H2>\d{1,2}):?(?P<M2>\d{1,2})? (?P<P2>AM|PM)'
    if match := re.search(pattern, s):
        # LOGIC
        hour1, minutes1, period1, hour2, minutes2, period2 = match.groups()
        hour1 = int(hour1)
        hour2 = int(hour2)
        if hour1 > 12 or hour2 > 12:
            raise ValueError
        elif minutes1 and (int(minutes1) > 59) or minutes2 and (int(minutes2) > 59):
            raise ValueError
        if period1 == "PM":
            hour1 += 12
        elif period2 == "PM" and hour2 != 12:
            hour2 += 12
        elif period1 == "AM" and hour1 == 12:
            hour1 = 0
        elif period2 == "AM" and hour2 == 12:
            hour2 = 0

        if minutes1 is not None and minutes2 is not None:
            return f"{hour1:02}:{minutes1:02} to {hour2:02}:{minutes2:02}"
        elif minutes1 is not None:
            return f"{hour1:02}:{minutes1:02} to {hour2:02}:00"
        elif minutes2 is not None:
            return f"{hour1:02}:00 to {hour2:02}:{minutes2:02}"
        else:
            return f"{hour1:02}:00 to {hour2:02}:00"
    else:
        raise ValueError



if __name__ == "__main__":
    main()