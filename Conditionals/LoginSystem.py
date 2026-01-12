user_name = "user" # setting a default user name 
password = "12345678" # setting a default password
user = input("Enter the user name : ") # taking input from user
if user == user_name: # validating user name as input
    pswd = input("Enter your password: ") # taking password from user
    if pswd == password: # checking if passwords match
        print("Login Successful")
    else: # handling incorrect password
        print("Incorrect Password")
        print("Login Failed")
else: # handling incorrect username 
    print("User doesn't exists")
