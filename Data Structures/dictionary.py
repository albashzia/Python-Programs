#defining a dictionary -- Structure = key -> value
book = {
    "title" : "Meditations",
    "author" : "Marcus Aurelius",
    "pages" : 120
}

#printing the values using keys
print(book["title"])
print(book["author"])
print(book["pages"])

#modifying the value of a key
book["pages"] = 90

#printing the whole dictionary values
print(book)

#deleting a key and its value
book.pop("pages")

#printing the dictionary
print(book)

#printing the keys of the dictionary
print(book.keys())

#printing the values of the dictionary
print(book.values())

#printing the items of the dictionary
print(book.items())

#accessing a non-existent key that returns "None" without crashing the code
print(book.get("pages"))