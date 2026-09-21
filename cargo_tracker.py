inventory = []
"""
This loop controls the main menu interface.
It will keep running until the user types '4' to exit.
"""
while True:
    print("Cargo Tracker Menu:")
    print("1. Add Cargo Item")
    print("2. View Cargo Items")
    print("3. Update Cargo Item Status")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        # This is blank place to save the cargo information
        item = {}
        item["id"] = input("Enter ID: ")
        item["weight"] = input("Enter Weight: ")
        item["destination"] = input("Enter the Destination: ")
        item["status"] = input("Enter the Status: ")
        item["name"] = input("Enter the Name: ")
        inventory.append(item)
    elif choice == "2":
        # This will show everything saved in the inventory list
        print("//////////////////////////////")
        print(f"Id is {item["id"]}")
        print(f"Weight is {item["weight"]}kg")
        print(f"Destination is {item["destination"]}")
        print(f"Status is {item["status"]}")
        print(f"Name is { item["name"]}")
        print("//////////////////////////////")
    elif choice == "3":
        lookup_id = input("Enter ID to update: ")

        # 1. Write "Not Found" on the sticky note before searching
        found = False

        # 2 & 3. Walk through the warehouse checking boxes
        for current_item in inventory:
            if current_item["id"] == lookup_id:
                new_status = input("Enter the new Status: ")
                current_item["status"] = new_status
                print("Status updated successfully!")

                # 4. We found it! Change the sticky note to "True"
                found = True
                break

        # 5. The search is over. Look at the sticky note.
        # If it still says "False", print the error.
        if found == False:
            print("Error: Cargo ID not found.")
