electricity_records = []

def calculate_bill(units):
    if units <= 100:
        amount = units * 3.5
    elif units <= 200:
        amount = 350 + (units - 100) * 4.5
    elif units <= 300:
        amount = 800 + (units - 200) * 6
    else:
        amount = 1400 + (units - 300) * 7.5
    return amount + 50

def add_record():
    cid = input("Enter Consumer ID: ")
    name = input("Enter Consumer Name: ")
    units = float(input("Enter Units: "))

    bill = calculate_bill(units)

    record = {
        "id": cid,
        "name": name,
        "units": units,
        "bill": bill
    }

    electricity_records.append(record)

    print("Record added successfully!")
    print("Bill Amount: Rs.", bill)

def view_records():
    if len(electricity_records) == 0:
        print("No records found.")
    else:
        for r in electricity_records:
            print("Consumer ID:", r["id"])
            print("Name:", r["name"])
            print("Units:", r["units"])
            print("Bill: Rs.", r["bill"])

while True:
    print("\n1. Add Record")
    print("2. View Records")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_record()
    elif choice == "2":
        view_records()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
      
