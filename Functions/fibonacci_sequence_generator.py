def fibonacci(n):
    a, b = 0, 1
    print(a, end=" ")
    while b <= n:
        print(b, end=" ")
        c = a + b
        a = b
        b = c

fibonacci(34)