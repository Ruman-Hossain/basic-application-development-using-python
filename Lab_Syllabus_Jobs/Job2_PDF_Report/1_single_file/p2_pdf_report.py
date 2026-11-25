import csv
import os
from fpdf import FPDF

FILE = "students.csv"
HEADER = ["Student_Id", "Name", "Roll", "Semester", "Shift", "Department", "Date of Birth", "Phone"]


def add_student():
    row = []
    for field in HEADER:
        row.append(input(field + ": ").strip())
    new_file = not os.path.exists(FILE)
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(HEADER)
        writer.writerow(row)
    print("Saved:", row[1])


def make_pdf():
    if not os.path.exists(FILE):
        print("No student saved yet!")
        return
    with open(FILE) as f:
        rows = list(csv.reader(f))
    header = rows[0]
    data = rows[1:]

    pdf = FPDF(orientation="L", format="A4")
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Pabna Polytechnic Institute", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 12)
    pdf.cell(0, 8, "Student Information Report - CST", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    widths = [28, 45, 25, 25, 20, 30, 35, 40]

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
    pdf.output("student_report.pdf")
    print("PDF created: student_report.pdf")


while True:
    print("\n1. Add student   2. Make PDF report   3. Exit")
    choice = input("Choose (1-3): ").strip()
    if choice == "1":
        add_student()
    elif choice == "2":
        make_pdf()
    elif choice == "3":
        print("Bye!")
        break
    else:
        print("Invalid choice!")
