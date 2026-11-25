import csv
from fpdf import FPDF

# Step 1: store student information in a CSV file
students = [
    ["Student_Id", "Name", "Roll", "Semester", "Shift", "Department", "Date of Birth", "Phone"],
    ["S001", "Rahim Uddin", "701234", "3rd", "1st", "CST", "12-05-2007", "01712345678"],
    ["S002", "Sumaiya Akter", "701235", "3rd", "1st", "CST", "03-09-2007", "01812345678"],
    ["S003", "Karim Hasan", "701236", "3rd", "2nd", "CST", "21-01-2008", "01912345678"],
]
with open("students.csv", "w", newline="") as f:
    csv.writer(f).writerows(students)
print("CSV saved: students.csv")

# Step 2: read the CSV file
with open("students.csv") as f:
    rows = list(csv.reader(f))
header = rows[0]
data = rows[1:]

# Step 3: create the PDF report
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
