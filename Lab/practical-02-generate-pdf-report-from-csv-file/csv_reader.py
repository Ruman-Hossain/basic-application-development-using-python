import csv
import os

def read_csv_data(filename="fruits_inventory.csv"):
    if not os.path.exists(filename):
        print("CSV file not found.")
        return []

    data = []

    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append({
                "fruit_name": row["fruit_name"],
                "unit_price": float(row["unit_price"]),
                "quantity": int(row["quantity"]),
                "total_price": float(row["total_price"])
            })

    return data