age = int(input("Enter the age: "))
status = input("Is the customer a student?(Y/N) : ").strip().lower()

if age < 18:
    if status == "y":
        print("Ticket Price = 150")
    elif status == "n":
        print("Ticket price = 200")
    else:
        print("Invalid Status")

elif age >=18:
    if status == "y":
        print("Ticket Price = 250")
    elif status == "n":
        print("Ticket price = 300")
    else:
        print("Invalid Status")
