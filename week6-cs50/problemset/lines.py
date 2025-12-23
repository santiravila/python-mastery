import sys

def main():
    error_message = validate_cla(sys.argv)
    if error_message:
        sys.exit(error_message)
    
    filename = sys.argv[1]
    try:
        lines = count_lines(filename)
        print(lines)
    except FileNotFoundError:
        sys.exit("File does not exist")


def validate_cla(arguments: list) -> str | None:
    if len(arguments) < 2:
        return "Too few command-line arguments"
    elif len(arguments) > 2:
        return "Too many command-line arguments"
    elif not arguments[1].endswith(".py"):
        return "Not a Python File"
    else:
        return None
  

def count_lines(filename):
    line_count = 0

    with open(filename, "r") as file:
        for line in file:

            # for indented comments
            stripped_line = line.lstrip()
            if stripped_line and not stripped_line.startswith("#"):
                line_count += 1

    return line_count


main()