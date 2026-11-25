import sqlite3

# Step 1: database and table
conn = sqlite3.connect("student.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS students (
                 roll TEXT PRIMARY KEY,
                 name TEXT NOT NULL,
                 department TEXT,
                 phone TEXT)""")
conn.commit()

# Step 2: functions for save, search and show
def save_data():
    roll = input("Roll: ").strip()
    name = input("Name: ").strip()
    dept = input("Department: ").strip()
    phone = input("Phone: ").strip()
    if roll == "" or name == "":
        print("Missing: Roll and Name are required")
        return
    try:
        cur.execute("INSERT INTO students VALUES (?, ?, ?, ?)",
                    (roll, name, dept, phone))
        conn.commit()
        print("Saved: Student saved successfully")
    except sqlite3.IntegrityError:
        print("Error: This roll already exists")

def search_data():
    roll = input("Enter roll to search: ").strip()
    cur.execute("SELECT * FROM students WHERE roll = ?", (roll,))
    row = cur.fetchone()
    if row:
        print("Found:", " | ".join(row))
    else:
        print("Not found: No student with roll " + roll)

def show_all():
    print("------ All Students ------")
    for row in cur.execute("SELECT * FROM students ORDER BY roll"):
        print(" | ".join(row))

# Step 3: menu (works in Google Colab, where no GUI window can open)
while True:
    print("\n1. Save   2. Search   3. Show all   4. Exit")
    choice = input("Choose (1-4): ").strip()
    if choice == "1":
        save_data()
    elif choice == "2":
        search_data()
    elif choice == "3":
        show_all()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")

conn.close()
print("Bye!")
