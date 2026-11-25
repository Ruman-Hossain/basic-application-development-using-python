import csv
import os

FILE = "fruits.csv"


def add_item():
    name = input("Fruit name: ").strip()
    try:
        price = float(input("Unit price (Tk): "))
        qty = int(input("Quantity (kg): "))
    except ValueError:
        print("Invalid number! Try again.")
        return
    total = price * qty
    new_file = not os.path.exists(FILE)
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["Fruit", "Unit Price", "Quantity", "Total Price"])
        writer.writerow([name, price, qty, total])
    print("Saved:", name, "| Total =", total, "Tk")


def show_summary():
    if not os.path.exists(FILE):
        print("No fruit saved yet!")
        return
    print("\n------ Fruit Inventory Summary ------")
    grand_total = 0
    total_qty = 0
    with open(FILE) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"{row['Fruit']:<10} {row['Unit Price']:>8} x {row['Quantity']:>3} = {row['Total Price']:>8} Tk")
            grand_total += float(row["Total Price"])
            total_qty += int(row["Quantity"])
    print("-------------------------------------")
    print("Total quantity :", total_qty, "kg")
    print("Grand total    :", grand_total, "Tk")


while True:
    print("\n1. Add fruit   2. Show summary   3. Exit")
    choice = input("Choose (1-3): ").strip()
    if choice == "1":
        add_item()
    elif choice == "2":
        show_summary()
    elif choice == "3":
        print("Bye!")
        break
    else:
        print("Invalid choice!")
