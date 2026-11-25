import tkinter as tk
from tkinter import messagebox

from .database import create_table, save_student, find_student, all_students


def run_app():
    """Build the student form window and start it."""
    create_table()

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

    listbox = tk.Listbox(root, width=55, height=8)

    def clear_form():
        for entry in entries:
            entry.delete(0, tk.END)

    def show_all():
        listbox.delete(0, tk.END)
        for row in all_students():
            listbox.insert(tk.END, " | ".join(row))

    def save_data():
        roll = e_roll.get().strip()
        name = e_name.get().strip()
        if roll == "" or name == "":
            messagebox.showwarning("Missing", "Roll and Name are required")
            return
        if save_student(roll, name, e_dept.get(), e_phone.get()):
            messagebox.showinfo("Saved", "Student saved successfully")
            clear_form()
            show_all()
        else:
            messagebox.showerror("Error", "This roll already exists")

    def search_data():
        roll = e_roll.get().strip()
        row = find_student(roll)
        if row:
            clear_form()
            for entry, value in zip(entries, row):
                entry.insert(0, value)
        else:
            messagebox.showinfo("Not found", "No student with roll " + roll)

    frame = tk.Frame(root)
    frame.grid(row=4, column=0, columnspan=2, pady=10)
    tk.Button(frame, text="Save", width=10, command=save_data).pack(side="left", padx=5)
    tk.Button(frame, text="Search", width=10, command=search_data).pack(side="left", padx=5)
    tk.Button(frame, text="Clear", width=10, command=clear_form).pack(side="left", padx=5)

    listbox.grid(row=5, column=0, columnspan=2, padx=10)
    show_all()

    root.mainloop()
