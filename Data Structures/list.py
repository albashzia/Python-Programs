numbers_list = [4,2,1,4,8,9,3,4,6,8,2,1,0]
words_list = ["Apple","Book","Shoes","Pen","Laptop","Fan"]

numbers_list.append(3)
words_list.append("Study")

numbers_list.insert(3,9)
words_list.insert(2,"Lamp")

numbers_list.remove(4)
words_list.remove("Laptop")

numbers_list.pop(4)
words_list.pop(1)

for i in numbers_list:
    print(i)

for j in words_list:
    print(j)

print(len(numbers_list))
print(len(words_list))

if 3 in numbers_list:
    print("Found")
else:
    print("Not found")

if "Pen" in words_list:
    print("Found")
else:
    print("Not found")

print(numbers_list.count(4))

numbers_list.sort()
for k in numbers_list:
    print(k)

words_list.reverse()
for l in words_list:
    print(l)