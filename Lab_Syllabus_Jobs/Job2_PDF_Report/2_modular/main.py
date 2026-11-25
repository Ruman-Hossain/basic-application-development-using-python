from report_tools import save_row, read_csv, make_pdf

FILE = "students.csv"
HEADER = ["Student_Id", "Name", "Roll", "Semester", "Shift", "Department", "Date of Birth", "Phone"]


def take_student():
    """Ask every field of one student and save it."""
    row = []
    for field in HEADER:
        row.append(input(field + ": ").strip())
    save_row(row, FILE, HEADER)
    print("Saved:", row[1])


def create_report():
    """Read the CSV and make the PDF report."""
    header, data = read_csv(FILE)
    if not data:
        print("No student saved yet!")
        return
    make_pdf(header, data, "student_report.pdf",
             "Pabna Polytechnic Institute", "Student Information Report - CST")
    print("PDF created: student_report.pdf")


if __name__ == "__main__":
    while True:
        print("\n1. Add student   2. Make PDF report   3. Exit")
        choice = input("Choose (1-3): ").strip()
        if choice == "1":
            take_student()
        elif choice == "2":
            create_report()
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice!")
