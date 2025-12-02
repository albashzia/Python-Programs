rows = 4
for r in range(rows):
    print(" " * (rows - r - 1) * 2, end="")
    for i in range(r + 1):
        print(2**i, end=" ")
    for i in range(r - 1, -1, -1):
        print(2**i, end=" ")
    print()
