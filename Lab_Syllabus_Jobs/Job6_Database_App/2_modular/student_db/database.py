import sqlite3

DB_FILE = "student.db"


def create_table():
    """Create the students table if it does not exist."""
    conn = sqlite3.connect(DB_FILE)
    conn.execute("""CREATE TABLE IF NOT EXISTS students (
                      roll TEXT PRIMARY KEY,
                      name TEXT NOT NULL,
                      department TEXT,
                      phone TEXT)""")
    conn.commit()
    conn.close()


def save_student(roll, name, department, phone):
    """Insert one student. Return True if saved, False if the roll already exists."""
    conn = sqlite3.connect(DB_FILE)
    try:
        conn.execute("INSERT INTO students VALUES (?, ?, ?, ?)",
                     (roll, name, department, phone))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def find_student(roll):
    """Return the student row as a tuple, or None if not found."""
    conn = sqlite3.connect(DB_FILE)
    row = conn.execute("SELECT * FROM students WHERE roll = ?", (roll,)).fetchone()
    conn.close()
    return row


def all_students():
    """Return a list of all student rows sorted by roll."""
    conn = sqlite3.connect(DB_FILE)
    rows = conn.execute("SELECT * FROM students ORDER BY roll").fetchall()
    conn.close()
    return rows
