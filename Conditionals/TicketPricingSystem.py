age = int(input("Enter the age: ")) # taking age as an input from the user 
status = input("Is the customer a student?(Y/N) : ").strip().lower() # taking customer's status from the user 

# handling condistion if age is less than 18
if age < 18:
    if status == "y": # handling if the customer is a student
        print("Ticket Price = 150")
    elif status == "n": # handling if the customer is not a student
        print("Ticket price = 200")
    else: # handling invalid input entered
        print("Invalid Status")

# handling if age is equal to or greater than 18
elif age >=18:
    if status == "y": # handling if the customer is a student
        print("Ticket Price = 250")
    elif status == "n": # handling if the customer is not a student
        print("Ticket price = 300")
    else: # handling invalid input entered
        print("Invalid Status")
