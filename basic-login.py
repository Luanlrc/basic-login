def acesso():
    user = input("Enter your username: ")
    password = input("Enter your password: ")
    if user == "luan" and password == "12345":
        print('User '+user+" and password "+password+" correct")
    else:
        print("Access denied")
        print("Try again")
        acesso() 

acesso()