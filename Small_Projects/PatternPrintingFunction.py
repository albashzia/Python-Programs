def pattern_A(rows):
    for i in range(1,rows+1):
        for j in range(1,i+1):
            print(j,end = " ")
        print()

def pattern_B(rows):
    for i in range(rows,0,-1):
        for j in range(1,i+1):
            print(j, end = " ")
        print()

def pattern_C(rows):
    for i in range(1,rows+1):
        spaces = rows - i
        print("  " * spaces, end="")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

rows = int(input("Enter number of rows : "))
choice = input("Enter the choice for pattern, A/B/C : ")
choice = choice.lower()
if choice == 'a':
    pattern_A(rows)
elif choice == 'b':
    pattern_B(rows)
elif choice == 'c':
    pattern_C(rows)
