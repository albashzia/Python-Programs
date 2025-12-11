str = input("Enter a string : ")
l = len(str)
new_str = ""
for i in range(l):
    if(i%2!=0):
        new_str = new_str+str[i]
print(new_str)
