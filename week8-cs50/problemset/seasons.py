"""
Input: date of birth in YYYY-MM-DD format (validation)
Output: 
- age in minutes
- rounded to the nearest integer
- using English words instead of numerals
- without any "and" between words
"""

DAY_MINUTE_CONVERSION = 1440

from datetime import date
import inflect
import sys


def main():
    try:
        birth_date = validate(input("Date of birth: "))
    except ValueError:
        sys.exit("Invalid date")
    
    print(f"{sing_minutes(minutes_from_birth(birth_date))} minutes")


def validate(raw_date):
    year, month, day = map(int, raw_date.split("-"))
    return date(year, month, day)
    

def minutes_from_birth(birth_date: date) -> int:
    date_difference = date.today() - birth_date
    return round(date_difference.days * DAY_MINUTE_CONVERSION)


def sing_minutes(minutes: int) -> str:
    p = inflect.engine()
    return p.number_to_words(minutes, andword="").capitalize()


if __name__ == "__main__":
    main()