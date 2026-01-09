# looping over a range from 1 to 9
for i in range(1,9):
    print("Table of",i) # printing a statement before printing each table
    # looping over a range from 1 to 10
    for k in range(1,11):
        print(i," x ",k," = ",i*k) # printing the actual statements
    k = k + 1 # incrementing k 
    i = i + 1 # incrementing i
