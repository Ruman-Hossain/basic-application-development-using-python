def print_summary(items):
    """Print every fruit and the totals."""
    print("\n------ Fruit Inventory Summary ------")
    grand_total = 0
    total_qty = 0
    for row in items:
        print(f"{row['Fruit']:<10} {row['Unit Price']:>8} x {row['Quantity']:>3} = {row['Total Price']:>8} Tk")
        grand_total += float(row["Total Price"])
        total_qty += int(row["Quantity"])
    print("-------------------------------------")
    print("Total quantity :", total_qty, "kg")
    print("Grand total    :", grand_total, "Tk")
