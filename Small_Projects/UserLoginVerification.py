user_name = "user"
password = int(87654321)
otp = int(1234)
entered_name = input("Enter Your user name : ")
entered_password = int(input("Enter your password: "))
entered_otp = int(input("Enter the OTP: "))
if(entered_name == user_name):
    if(entered_password == password):
        if(entered_otp == otp):
            print("Login Succeddful")
        else:
            print("Incorrect Otp")
    else:
        print("Incorrect Password")
else:
    print("User Name doesn't exits")