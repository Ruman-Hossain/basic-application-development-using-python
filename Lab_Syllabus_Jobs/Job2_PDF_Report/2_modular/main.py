from report_tools import save_csv, read_csv, make_pdf

students = [
    ["Student_Id", "Name", "Roll", "Semester", "Shift", "Department", "Date of Birth", "Phone"],
    ["S001", "Rahim Uddin", "701234", "3rd", "1st", "CST", "12-05-2007", "01712345678"],
    ["S002", "Sumaiya Akter", "701235", "3rd", "1st", "CST", "03-09-2007", "01812345678"],
    ["S003", "Karim Hasan", "701236", "3rd", "2nd", "CST", "21-01-2008", "01912345678"],
]

if __name__ == "__main__":
    save_csv(students, "students.csv")
    print("CSV saved: students.csv")

    header, data = read_csv("students.csv")
    make_pdf(header, data, "student_report.pdf",
             "Pabna Polytechnic Institute", "Student Information Report - CST")
    print("PDF created: student_report.pdf")
