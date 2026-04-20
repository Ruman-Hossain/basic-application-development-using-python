import csv
import os

def print_fruits_summary(filename="fruits_inventory.csv"):
    if not os.path.exists(filename) or os.stat(filename).st_size == 0:
        print("No fruit items to display.")
        return

    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        if not reader.fieldnames:
            print("CSV file has no headers.")
            return

        try:
            print(f"{'Fruit Name':<15}{'Unit Price':<15}{'Quantity':<10}{'Total Price'}")
            print('-' * 50)

            found_data = False
            for row in reader:
                found_data = True
                print(
                    f"{row['fruit_name']:<15}"
                    f"{float(row['unit_price']):<15}"
                    f"{int(row['quantity']):<10}"
                    f"{float(row['total_price']):.2f}"
                )

            if not found_data:
                print("No data rows found.")

        except KeyError as e:
            print(f"Missing column: {e}")
        except Exception as e:
            print(f"Error: {e}")