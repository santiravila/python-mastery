import sys
import csv


def main():
    error_message = validate_cla(sys.argv)
    if error_message:
        sys.exit(error_message)

    infilename = sys.argv[1]
    outfilename = sys.argv[2]
    try:
        with open(infilename, "r") as infile, open(outfilename, "w", newline='') as outfile:
            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
            writer.writeheader()
            
            for row in reader:
                last, first = row["name"].split(",")
                new_row = {
                    "first": first.lstrip(),
                    "last": last,
                    "house": row["house"]
                    }
                writer.writerow(new_row)     

    except FileNotFoundError:
        sys.exit(f"Could not read {infilename}")
    

def validate_cla(arguments: list) -> str | None:
    if len(arguments) < 3:
        return "Too few command-line arguments"
    elif len(arguments) > 3:
        return "Too many command-line arguments"
    else:
        return None
    

main()