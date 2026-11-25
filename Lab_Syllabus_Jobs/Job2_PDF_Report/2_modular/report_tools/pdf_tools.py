from fpdf import FPDF

WIDTHS = [28, 45, 25, 25, 20, 30, 35, 40]


def make_pdf(header, data, filename, title, subtitle, widths=WIDTHS):
    """Make a landscape A4 PDF with a title and a table."""
    pdf = FPDF(orientation="L", format="A4")
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, title, align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 12)
    pdf.cell(0, 8, subtitle, align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    pdf.set_font("Helvetica", "B", 10)
    pdf.set_fill_color(200, 220, 255)
    for i in range(len(header)):
        pdf.cell(widths[i], 9, header[i], border=1, align="C", fill=True)
    pdf.ln()

    pdf.set_font("Helvetica", "", 10)
    for row in data:
        for i in range(len(row)):
            pdf.cell(widths[i], 8, row[i], border=1, align="C")
        pdf.ln()

    pdf.ln(4)
    pdf.cell(0, 8, "Total students: " + str(len(data)))
    pdf.output(filename)
