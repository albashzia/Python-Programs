print("Largest of Three Numbers")
# taking input from the user 
num1 = input("Enter 1st Number ; ")
num2 = input("Enter 2nd Number ; ")
num3 = input("Enter 3rd Number ; ")
# checking if num1 is greater than other 2
if( num1 >= num2 and num1 >= num3):
    print("Number 1 is largest :", num1)
# checking if num2 is greater than num 3
elif (num2 >= num3):
    print("Number 2 is largest :", num2)
# executing else statement 
else:
    print("Number 3 is largest :", num3)