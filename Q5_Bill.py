def generate_grocery_bill():
    items = []  
    total_amount = 0  

    while True:
        item_name = input("Enter the name of the item: ")
        item_quantity = int(input("Enter the quantity purchased: "))
        item_price = float(input("Enter the price per unit: "))

        item_total = item_quantity * item_price
        total_amount += item_total

        items.append((item_name, item_quantity, item_price, item_total))

        more_items = input("Do you want to add another item? (yes/no): ")
        if more_items.lower() != 'yes':
            break

    print("\n* * * * BILL * * * *")
    print(f"{'Item Name':<15}{'Item Quantity':<15}{'Item Price':<15}{'Total Price':<15}")
    print("*" * 50)

    for item in items:
        print(f"{item[0]:<15}{item[1]:<15}{item[2]:<15.2f}{item[3]:<15.2f}")

    print("*" * 50)
    print(f"Total Amount to be paid: {total_amount:.2f}")
    print("*" * 50)

generate_grocery_bill()