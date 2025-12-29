score = int(input("Enter your score: "))
if score > 100:
    print("Invalid Score")
elif score >= 90:
    print("A+")
elif score >= 85:
    print("A")
elif score >= 75:
    print("B")
elif score >= 65:
    print("C")
elif score >= 50:
    print("D")
elif score < 50:
    print("F")
