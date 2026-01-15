# taking input from the user 
str = input("Enter a string : ")
# storing length of input string in a variable 
l = len(str)
# decalring an empty string
new_str = ""
for i in range(l):
    if(i%2!=0): # filtering odd index element 
        new_str = new_str+str[i] # adding the elements at odd index to new_str
print(new_str) # printing new_str 
