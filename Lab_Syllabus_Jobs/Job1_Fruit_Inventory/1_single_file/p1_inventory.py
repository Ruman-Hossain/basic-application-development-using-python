import csv
import os

FILE = "fruits.csv"

def add_items():
    new_file = not os.path.exists(FILE)
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["Fruit", "Unit Price", "Quantity", "Total Price"])
        while True:
            name = input("Fruit name (q to quit): ").strip()
            if name.lower() == "q":
                break
            try:
                price = float(input("Unit price (Tk): "))
                qty = int(input("Quantity (kg): "))
            except ValueError:
                print("Invalid number! Try again.")
                continue
            total = price * qty
            writer.writerow([name, price, qty, total])
            print("Saved:", name, "| Total =", total, "Tk")

def show_summary():
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

add_items()
show_summary()
