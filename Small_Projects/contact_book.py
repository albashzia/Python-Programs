contacts = {
    "Muhammad Ali": "+92-300-1234567",
    "Ayesha Khan": "+92-321-7654321",
    "Zainab Ahmed": "+92-333-9876543",
    "Bilal Shah": "+92-345-1122334",
    "Fatima Malik": "+92-312-5566778",
    "Hamza Hussain": "+92-301-4433221",
    "Yousaf": "+92-322-8899001",
    "Omer Farooq": "+92-334-2233445",
    "Amna": "+92-346-6677889",
    "Usman Raza": "+92-313-9988776",
    "Mariam Javed": "+92-302-3344556",
    "Asad Mahmood": "+92-323-5544332",
    "Hira Iqbal": "+92-335-7788990",
    "Zeeshan Tariq": "+92-347-1133557",
    "Rehman": "+92-314-2244668"
}

def menu():
    print(
          "\n1. Add Contact "
          "\n2. Search Contact "
          "\n3. Update Contact"
          "\n4. Delete Contact"
          "\n5. View All Contacts"
          "\n6. Exit"
          )

def add():
    name = input("Enter name:")
    number = input("Enter phone number:")
    contacts[name] = number
    print(f'Successfully added {name} to the contact book.')

def search():
    name_entered = input("Enter name:")
    if name_entered in contacts:
        print(f'Name = {name_entered}, Phone Number = {contacts[name_entered]}')
    else:
        print(f'Contact {name_entered} not found in contact book.')

def update():
    name_entered = input("Enter the name of contact to be updated: ")
    if name_entered in contacts:
        new_number = input("Enter new number:")
        contacts[name_entered] = new_number
        print(f'Contact {name_entered} updated with number {new_number}')
    else:
        print(f'Contact {name_entered} not found in contact book.')

def delete():
    name_entered = input("Enter the name of contact to be deleted:")
    if name_entered in contacts:
        contacts.pop(name_entered)
        print(f'Contact {name_entered} deleted from the contact book.')
    else:
        print(f'Contact {name_entered} not found in contact book.')

def view_all():
    for name,number in contacts.items():
        print(f'Name = {name}, Number = {number}')
    print("\nEnd of Contact Book Reached")

while True:
    print("=====================")
    print("    Contact Book")
    print("=====================")
    menu()
    num = int(input("Enter the number: "))
    if num==1:
        add()
    elif num==2:
        search()
    elif num==3:
        update()
    elif num==4:
        delete()
    elif num==5:
        view_all()
    elif 6:
        print("Exiting the contact book.")
        exit()