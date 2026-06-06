book = {
    "title" : "Meditations",
    "author" : "Marcus Aurelius",
    "pages" : 120
}

print(book["title"])
print(book["author"])
print(book["pages"])

book["pages"] = 90

print(book)

book.pop("pages")

print(book)

print(book.keys())
print(book.values())
print(book.items())