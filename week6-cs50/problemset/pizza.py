import csv
import sys
from tabulate import tabulate


def main():
    error_message = validate_cla(sys.argv)
    if error_message:
        sys.exit(error_message)

    filename = sys.argv[1]
    try:
        print(get_formatted_table(filename))
    except FileNotFoundError:
        sys.exit("File does not exist")


def validate_cla(arguments: list) -> str | None:
    if len(arguments) < 2:
        return "Too few command-line arguments"
    elif len(arguments) > 2:
        return "Too many command-line arguments"
    elif not arguments[1].endswith(".csv"):
        return "Not a CSV File"
    else:
        return None


def get_formatted_table(filename) -> str:
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        return tabulate(list(reader), headers="keys", tablefmt="grid")


main()