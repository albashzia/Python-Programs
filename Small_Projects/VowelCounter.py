Str = input("Enter a string: ")
Str = Str.lower()
l = len(Str)
count = 0
for i in range(l):
    if Str[i] == 'a' or Str[i] == 'e' or Str[i] == 'i' or Str[i] == 'o' or Str[i] == 'u':
        count = count + 1
print("The number of vowels present is given string is ",count)
