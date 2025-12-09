def largest(a, b, c, d):
    largest_num = a
    if b > largest_num:
        largest_num = b
    if c > largest_num:
        largest_num = c
    if d > largest_num:
        largest_num = d
    return largest_num

print(largest(10, 25, 7, 18))