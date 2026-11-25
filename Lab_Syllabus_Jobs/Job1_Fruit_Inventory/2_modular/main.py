from fruit_inventory import add_item, read_items, print_summary


def take_input():
    """Take fruit data from the user until q is entered."""
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
        total = add_item(name, price, qty)
        print("Saved:", name, "| Total =", total, "Tk")


if __name__ == "__main__":
    take_input()
    print_summary(read_items())
