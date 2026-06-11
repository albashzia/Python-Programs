string1 = "the quick brown fox"

print(string1.upper())
print(string1.title())

string2 = "JUMPED OVER THE LAZY DOG"
print(string2.lower())

string3 = "   I like Java     "
print(string3)
print(string3.strip())
string3.replace("Java","Python")
print(string3.replace("Java","Python").strip())

words = string1.split()
print(words)

print(string1.startswith("the"))
print(string2.endswith("DOG"))