salary = float(input("Enter the salary: "))
if( salary >= 30000):
    salary = salary - (salary*0.08)
elif(salary >= 15000):
    salary = salary - 1000
else:
    salary = salary
print("The final salary is",salary)