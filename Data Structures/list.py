# Initializing the lists
numbers_list = [4,2,1,4,8,9,3,4,6,8,2,1,0]
words_list = ["Apple","Book","Shoes","Pen","Laptop","Fan"]

# Appending to lists
numbers_list.append(3)
words_list.append("Study")

# Inserting to lists at specific index
numbers_list.insert(3,9)
words_list.insert(2,"Lamp")

# Removing the elements from lists using values
numbers_list.remove(4)
words_list.remove("Laptop")

#Removing the elements from lists using index
numbers_list.pop(4)
words_list.pop(1)

# Printing the elements of the lists

print("\nElements of Numbers list: ")
for i in numbers_list:
    print(i)

print("\nElements of Words list: ")
for j in words_list:
    print(j)

# Printing the lengths of the lists

print("\nLength of Numbers list: ")
print(len(numbers_list))

print("\nLength of Words list: ")
print(len(words_list))

# Checking the existence of specified elements in the lists

print("\nElement 3 in Numbers list: ")
if 3 in numbers_list:
    print("Found")
else:
    print("Not found")

print("\nWord 'Pen' in Numbers list: ")
if "Pen" in words_list:
    print("Found")
else:
    print("Not found")

# Counting the intensity of an element in the list
print("\nCount of 4 in Numbers list: ")
print(numbers_list.count(4))

# Sorting the elements of the list
print("\nSorted Elements of  Numbers list: ")
numbers_list.sort()
for k in numbers_list:
    print(k)

# Reversing the elements of list
print("\nReversed Elements of Words list: ")
words_list.reverse()
for l in words_list:
    print(l)