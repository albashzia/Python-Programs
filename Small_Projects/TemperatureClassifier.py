temp = float(input("Enter the temperature: "))
if(temp>35):
    print("Hot Day")
elif(temp>=25 and temp<=35):
    print("Pleasant Day")
elif(temp>=18 and temp<=24):
    print("Cool Day")
elif(temp<18):
    print("Cold Day")