units_consumed = float(input("Enter units consumed: "))
if( units_consumed <= 400):
    cost = 3
elif(units_consumed > 400 and units_consumed <= 600):
    cost = 5
else:
    cost = 8
print("The total bill is ",(units_consumed*cost)+200)