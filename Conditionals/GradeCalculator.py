score = int(input("Enter your score: ")) # taking grade as an input from the user

# tackling invalid entered score i.e greater than 100
if score > 100: 
    print("Invalid Score")

# printing A+ if score is greater than or equal to 90
elif score >= 90:
    print("A+")

# printing A if score is greater than or equal to 85
elif score >= 85:
    print("A")

# printing B if score is greater than or equal to 75
elif score >= 75:
    print("B")

# printing C if score is greater than or equal to 65
elif score >= 65:
    print("C")

# printing D if score is greater than or equal to 50
elif score >= 50:
    print("D")
    
# printing F if score is less than 50
elif score < 50:
    print("F")
