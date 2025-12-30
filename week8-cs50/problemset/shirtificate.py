"""
Input: user's name
Output: A pdf with text overlaid over the shirt image.
- orientation: Portrait. (default)
- PDF format: A4 (default)
- "CS50 Shirtificate" centered horizontally at the top
- shirt's image centered horizontally.
- user's name on top of the shirt in white text.
"""
from fpdf import FPDF

class ShirtificatePDF(FPDF):

    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_auto_page_break(False)

    def header(self):
        self.set_font("Helvetica", "B", 32)
        self.cell(0, 40, "CS50 Shirtificate", align="C")
        self.ln(10)

    def add_shirt(self):
        self.image("shirtificate.png", x=0, y=60, w=210)

    def add_name_text(self, name: str):
        self.set_font("Helvetica", "B", 24)
        self.set_text_color(255, 255, 255)

        self.set_y(140)
        self.cell(0, 10, f"{name} took CS50", align="C")


def main():
    name = input("Name: ")

    pdf = ShirtificatePDF()
    pdf.add_page()
    pdf.add_shirt()
    pdf.add_name_text(name)

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
