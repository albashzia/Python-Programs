# taking input from user
Str = input("Enter a string: ")
# converting the string to lowercase
Str = Str.lower()
# storing length of string in l variable
l = len(Str)
# counter to count the number of variables
count = 0
# looping over the entire string
for i in range(l):
    # checking for presence of vowels in the string
    if Str[i] == 'a' or Str[i] == 'e' or Str[i] == 'i' or Str[i] == 'o' or Str[i] == 'u':
        # incrementing coun tvariable if vowel is found
        count = count + 1
# printing the number of vowels at end after looping over the whole string
print("The number of vowels present is given string is ",count)
