inventory = {}

while True:
    print ("\n=====INVENTORY MENU=====")
    print ("[1] Add Item")
    print ("[2] Update Item")
    print ("[3] Delete Item")

    choice = input("Choice: ")

    if choice == '1':
        item = input("Enter item name to add: ")
        price = float(input("Enter price: "))
        inventory[item] = price
        print(f"Item added sucessfully")

    elif choice == '2':
        item = input("Enter item name to update: ")
        if item in inventory:
            price = float(input("Enter new price: "))
            inventory[item] = price
            print(f"Price updated successfully.")
        else:
            print(f"Item not found in inventory.")

    elif choice == '3':
        print("Exitting system...")
        break

    else:
        print("Invalid choice. Please try again.")