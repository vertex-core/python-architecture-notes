# 1. Set up the empty list to hold our data
inventory = []


# 2. Define the specialized departments (Functions)
def add_cargo(inventory):
    item = {}
    item["id"] = input("Enter ID: ")
    item["weight"] = input("Enter Weight: ")
    item["destination"] = input("Enter the Destination: ")
    item["status"] = input("Enter the Status: ")
    item["name"] = input("Enter the Name: ")
    inventory.append(item)
    print("Cargo added successfully!")


# 3. Define the main menu interface
def menu(inventory):
    while True:
        print("\n--- Cargo Tracker Menu ---")
        print("1. Add Cargo Item")
        print("2. View Cargo Items")
        print("3. Update Cargo Item Status")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            # We call the function we built at the top
            add_cargo(inventory)

        elif choice == "2":
            # Loop through and print every item in the list
            for item in inventory:
                print("////////////////////////////////")
                print(f"Id is {item['id']}")
                print(f"Weight is {item['weight']}kg")
                print(f"Destination is {item['destination']}")
                print(f"Status is {item['status']}")
                print(f"Name is {item['name']}")
                print("////////////////////////////////")

        elif choice == "3":
            # Search for a specific ID and update it
            lookup_id = input("Enter ID to update: ")
            found = False

            for current_item in inventory:
                if current_item["id"] == lookup_id:
                    new_status = input("Enter the new Status: ")
                    current_item["status"] = new_status
                    print("Status updated successfully!")
                    found = True
                    break

            if found == False:
                print("Error: Cargo ID not found.")

        elif choice == "4":
            print("Exiting Cargo Tracker. Goodbye!")
            break

        else:
            print("Invalid input. Please type 1, 2, 3, or 4.")


# 4. Press the "Start" button to actually run the program
menu(inventory)
