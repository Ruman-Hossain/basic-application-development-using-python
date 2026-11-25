import csv
import os

FILE = "fruits.csv"
HEADER = ["Fruit", "Unit Price", "Quantity", "Total Price"]


def add_item(name, price, qty, file=FILE):
    """Save one fruit in the CSV file and return its total price."""
    new_file = not os.path.exists(file)
    total = price * qty
    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(HEADER)
        writer.writerow([name, price, qty, total])
    return total


def read_items(file=FILE):
    """Read all fruits from the CSV file as a list of dictionaries."""
    with open(file) as f:
        return list(csv.DictReader(f))
