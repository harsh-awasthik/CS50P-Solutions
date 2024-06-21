from fpdf import FPDF

class pdf(FPDF):
    def add_title(self, title):
        self.set_font("helvetica", "B", 30)
        width = self.get_string_width(title) + 4
        x = (210-width)/2
        self.set_xy(x,10)
        self.cell(width, 30, title, align="C")

    def add_img(self):
        self.image("shirtificate.png", 0, 50)

    def add_text(self, name):
        text = name + " took CS50"
        self.set_font("helvetica", "B", 20)
        self.set_text_color(255,255,255)
        width = self.get_string_width(text) + 4
        x = (210 - width)/2
        y = (297)/3
        self.set_xy(x,y)
        self.cell(width, 20, text, align = "C")

p = pdf()
p.add_page()
p.add_img()
p.add_title("CS50 Shirtificate")
p.add_text(input("Name: "))
p.output("shirtificate.pdf")
