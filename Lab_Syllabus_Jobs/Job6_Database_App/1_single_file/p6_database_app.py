import sqlite3
import tkinter as tk
from tkinter import messagebox

# Step 1: database and table
conn = sqlite3.connect("student.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS students (
                 roll TEXT PRIMARY KEY,
                 name TEXT NOT NULL,
                 department TEXT,
                 phone TEXT)""")
conn.commit()

# Step 4: button functions
def save_data():
    roll = e_roll.get().strip()
    name = e_name.get().strip()
    if roll == "" or name == "":
        messagebox.showwarning("Missing", "Roll and Name are required")
        return
    try:
        cur.execute("INSERT INTO students VALUES (?, ?, ?, ?)",
                    (roll, name, e_dept.get(), e_phone.get()))
        conn.commit()
        messagebox.showinfo("Saved", "Student saved successfully")
        clear_form()
        show_all()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "This roll already exists")

def search_data():
    roll = e_roll.get().strip()
    cur.execute("SELECT * FROM students WHERE roll = ?", (roll,))
    row = cur.fetchone()
    if row:
        clear_form()
        e_roll.insert(0, row[0])
        e_name.insert(0, row[1])
        e_dept.insert(0, row[2])
        e_phone.insert(0, row[3])
    else:
        messagebox.showinfo("Not found", "No student with roll " + roll)

def clear_form():
    for entry in (e_roll, e_name, e_dept, e_phone):
        entry.delete(0, tk.END)

def show_all():
    listbox.delete(0, tk.END)
    for row in cur.execute("SELECT * FROM students ORDER BY roll"):
        listbox.insert(tk.END, " | ".join(row))

# Step 2: design the form
root = tk.Tk()
root.title("Student Database")
root.geometry("460x400")

labels = ["Roll", "Name", "Department", "Phone"]
entries = []
for i, text in enumerate(labels):
    tk.Label(root, text=text, font=("Arial", 11)).grid(row=i, column=0, padx=10, pady=6, sticky="w")
    entry = tk.Entry(root, width=30, font=("Arial", 11))
    entry.grid(row=i, column=1, padx=10, pady=6)
    entries.append(entry)
e_roll, e_name, e_dept, e_phone = entries

# Step 3: command buttons
frame = tk.Frame(root)
frame.grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(frame, text="Save", width=10, command=save_data).pack(side="left", padx=5)
tk.Button(frame, text="Search", width=10, command=search_data).pack(side="left", padx=5)
tk.Button(frame, text="Clear", width=10, command=clear_form).pack(side="left", padx=5)

listbox = tk.Listbox(root, width=55, height=8)
listbox.grid(row=5, column=0, columnspan=2, padx=10)
show_all()

root.mainloop()
conn.close()
