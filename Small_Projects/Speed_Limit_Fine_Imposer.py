#This program will take various speed inputs and impose fine over a certain limit
speed = int(input("Please enter the recorded speed : "))
if(speed<120 and speed>0):
    print("No fine, Speed under limit")
elif(speed<0):
    print("Invalid Speed")
elif(speed>120):
    print("Speed violation")
    if(speed>=120 and speed<150):
        print("The fine amount is Rs 3000")
    if(speed>=150 and speed<180):
        print("The fine is Rs 5000")
    if(speed>=180):
        print("The license to be confiscated under the law along with Rs 10,000 fine")