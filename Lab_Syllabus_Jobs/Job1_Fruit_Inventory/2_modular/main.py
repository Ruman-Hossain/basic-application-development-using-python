from fruit_inventory import add_item, read_items, print_summary


def take_item():
    """Take one fruit from the user and save it."""
    name = input("Fruit name: ").strip()
    try:
        price = float(input("Unit price (Tk): "))
        qty = int(input("Quantity (kg): "))
    except ValueError:
        print("Invalid number! Try again.")
        return
    total = add_item(name, price, qty)
    print("Saved:", name, "| Total =", total, "Tk")


if __name__ == "__main__":
    while True:
        print("\n1. Add fruit   2. Show summary   3. Exit")
        choice = input("Choose (1-3): ").strip()
        if choice == "1":
            take_item()
        elif choice == "2":
            print_summary(read_items())
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice!")
