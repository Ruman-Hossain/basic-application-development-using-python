def format_table_data(data):
    table_data = [["Fruit", "Unit Price", "Quantity", "Total Price"]]

    for item in data:
        table_data.append([
            item["fruit_name"],
            f"{item['unit_price']:.2f}",
            item["quantity"],
            f"{item['total_price']:.2f}"
        ])

    return table_data