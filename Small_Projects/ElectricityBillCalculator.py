units_consumed = float(input("Enter units consumed: ")) # taking input from user 
if( units_consumed <= 400): # evaluating condition if units are less or equal to 400
    cost = 3
elif(units_consumed > 400 and units_consumed <= 600): # evaluating if units are greater than 400 and less than 600
    cost = 5
else:
    cost = 8
print("The total bill is ",(units_consumed*cost)+200) # calculating and printing final bill