def sum(a,b):
    print(a+b)

def difference(a,b):
    print(a-b)

def product(a,b):
    print(a*b)

def quotient(a,b):
    print(a/b)

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
choice = input("Enter choice of operation to perform +,-,*,/ : ")
if choice == '+':
    sum(num1,num2)
if choice == '-':
    difference(num1,num2)
if choice == '*':
    product(num1,num2)
if choice == '/':
    quotient(num1,num2)
        
