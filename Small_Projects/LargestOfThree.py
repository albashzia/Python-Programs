print("Largest of Three Numbers")

num1 = input("Enter 1st Number ; ")
num2 = input("Enter 2nd Number ; ")
num3 = input("Enter 3rd Number ; ")
if( num1 >= num2 and num1 >= num3):
    print("Number 1 is largest :", num1)
elif (num2 >= num3):
    print("Number 2 is largest :", num2)
else:
    print("Number 3 is largest :", num3)