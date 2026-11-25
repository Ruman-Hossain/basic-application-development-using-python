import csv
import os

def store_data_to_csv(data, filename="fruits_inventory.csv"):
    field_names = ["fruit_name", "unit_price", "quantity", "total_price"]
    file_exists = os.path.exists(filename)

    with open(filename, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)

        if not file_exists or csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow(data)