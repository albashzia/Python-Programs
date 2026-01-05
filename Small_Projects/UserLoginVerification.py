# setting default user_name, password and otp
user_name = "user"
password = int(87654321)
otp = int(1234)

# taking username, password and otp from the user
entered_name = input("Enter Your user name : ")
entered_password = int(input("Enter your password: "))
entered_otp = int(input("Enter the OTP: "))

# comparing entered inputs with default values using conditionals using user_name
if(entered_name == user_name):
    # comparing entered inputs with default values using conditionals using password
    if(entered_password == password):
        # comparing entered inputs with default values using conditionals using otp
        if(entered_otp == otp):
            print("Login Succeddful")
        else:
            print("Incorrect Otp")
    else:
        print("Incorrect Password")
else:
    print("User Name doesn't exits")
