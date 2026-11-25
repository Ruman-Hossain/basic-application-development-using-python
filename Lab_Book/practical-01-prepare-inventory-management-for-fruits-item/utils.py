import os

def reset_inventory_file(filename="fruits_inventory.csv"):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"'{filename}' has been deleted.")
    else:
        print(f"'{filename}' does not exist, no action needed.")