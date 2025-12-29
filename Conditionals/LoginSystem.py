user_name = "user"
password = "12345678"
user = input("Enter the user name : ")
if user == user_name:
    pswd = input("Enter your password: ")
    if pswd == password:
        print("Login Successful")
    else:
        print("Incorrect Password")
        print("Login Failed")
else:
    print("User doesn't exists")
