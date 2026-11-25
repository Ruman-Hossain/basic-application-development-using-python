def get_fruit_data():
    fruit_name = input("Enter Fruit Name: ")
    unit_price = float(input("Enter Unit Price: "))
    quantity = int(input("Enter Quantity: "))
    total_price = unit_price * quantity

    return {
        "fruit_name": fruit_name,
        "unit_price": unit_price,
        "quantity": quantity,
        "total_price": total_price
    }