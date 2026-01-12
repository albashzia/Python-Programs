a = int(input("Enter 1st number: ")) # taking first number as input from the user
b = int(input("Enter 2nd number: ")) # taking second number as input from user
if(a>b): # checking if a is greater than b 
    print(a,"is greater than",b)
elif(a<b): # checking if a is less than b
    print(a,"is less than",b)
else: # handling if both a and b are equal 
    print(a,"and",b,"are equal")
