def largest(a,b,c):
    if( a > b and a > c):
        print("Number 1 is largest :", a)
    elif (b > c):
        print("Number 2 is largest :", b)
    else:
        print("Number 3 is largest :", c)

num1 = input("Enter 1st Number ; ")
num2 = input("Enter 2nd Number ; ")
num3 = input("Enter 3rd Number ; ")
largest(num1,num2,num3)
