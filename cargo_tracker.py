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
    if choice == "2":
        print("//////////////////////////////")
        print(f"Id is {item["id"]}")
        print(f"Weight is {item["weight"]}kg")
        print(f"Destination is {item["destination"]}")
        print(f"Status is {item["status"]}")
        print(f"Name is { item["name"]}")
        print("//////////////////////////////")
