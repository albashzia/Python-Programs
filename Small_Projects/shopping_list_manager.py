shopping_list = []

def menu():
    print(
        "\n1. Add Item"
        "\n2. Remove Item"
        "\n3. View Shopping List"
        "\n4. Search Item"
        "\n5. Count Items"
        "\n6. Clear List"
        "\n7. Exit"
    )

def add_item():
    item = input("Enter the item to add to list: ")
    shopping_list.append(item)

def remove_item():
    item = input("Enter the item to remove from list: ")
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print("Item not found in list.")

def view_list():
    for i in shopping_list:
        print(i)

def search_item():
    item = input("Enter name of item to search:")
    if item in shopping_list:
        print(f"Item Found at index {shopping_list.index(item)}")
    else:
        print("Item not found.")

def count_items():
    print(f'The number of items in list is {len(shopping_list)}')