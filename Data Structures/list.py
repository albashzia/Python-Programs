numbers_list = [4,2,1,4,8,9,3,4,6,8,2,1,0]
words_list = ["Apple","Book","Shoes","Pen","Laptop","Fan"]

numbers_list.append(3)
words_list.append("Study")

numbers_list.insert(3,9)
words_list.insert(2,"Lamp")

numbers_list.remove(4)
words_list.remove("Laptop")
for i in numbers_list:
    print(i)

for j in words_list:
    print(j)