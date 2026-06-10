number_set1 = {1,2,3,4,5,6,4,3,2,4,2}
number_set2 = {10,11,12,23,45,67,3,2,5,6,2,6,1,3,6}

words_set = {"book","bag","shoes","laptop","book"}

words_set.add("keys")

words_set.remove("bag")

number_set1.pop()

number_set3 = number_set1.union(number_set2)
print(number_set3)

number_set4 = number_set1.intersection(number_set2)
print(number_set4)