import csv
import numpy as np
from PIL import Image


def main():
    with open("views.csv", "r") as view, open("analysis.csv", "w") as analysis:
        reader = csv.DictReader(view)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()

        for row in reader:
            row["brightness"] = calculate_brightness(f"{row['id']}.jpeg")
            writer.writerow(row)
            

def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()