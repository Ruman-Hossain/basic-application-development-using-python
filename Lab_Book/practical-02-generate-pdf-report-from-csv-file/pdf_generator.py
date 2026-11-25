from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def generate_pdf(data, filename="report.pdf"):
    document = SimpleDocTemplate(filename)

    table = Table(data)

    style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),

        ("ALIGN", (0, 0), (-1, -1), "CENTER"),

        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ])

    table.setStyle(style)

    document.build([table])