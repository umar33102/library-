users = []

def register():
    print("Register: ")
    userName = input("Enter Your Name: ")
    password = input("Enter the Password: ")
    if not userName or not password:
        print("Please Enter Your Name: ")
        return
    newUser = {
        "Name" : userName,
        'Password' : password
    }
    users.append(newUser)
    print(f"User '{userName}' successfully Register! ")
    

def login():
    print("Login: ")
    userName = input("Enter Your Name: ")
    userFound = False
    for user in users:
        if user['name'] == userName:
            userFound = user
            break
    if not userFound:
        print("User not Found: ")
        return
    password = input("Enter Your Password: ")
    if userFound['password'] == password:
        print(f"Welcome back, {userName}")

def main():
    while True:
        print("Welcome to the Login and Registration System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = int(input("Enter your choice (1/2/3)"))
        if choice == 1:
            register()
        elif choice == 2:
            login()
        elif choice == 3:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("invalid choice. please try again. \n")

if __name__ == '__main__':
    main()


            
