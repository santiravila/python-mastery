MONTHS = { 
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

def main():
    while True:
        date = input("Date: ")
        try:
            if "/" in date:
                month, day, year = map(int, date.split('/'))
                if month > 12 or day > 31:
                    continue
            else:
                if "," not in date:
                    continue
                date = date.replace(",", '')
                month, day, year = date.split(" ")
                day = int(day)
                if day > 31:
                    continue
                month = MONTHS[month]
        except KeyError:
            pass
        except ValueError:
            pass
        else:
            print(f"{year}-{month:02}-{day:02}")
            return

main()
