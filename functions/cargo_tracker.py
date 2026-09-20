inventory = []
while True:
    print("Cargo Tracker Menu:")
    print("1. Add Cargo Item")
    print("2. View Cargo Items")
    print("3. Update Cargo Item Status")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        item = {}
    item["id"] = input("Enter ID:")
