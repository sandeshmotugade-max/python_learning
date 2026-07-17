password = ""

while True:
    password = input("Enter Password: ")

    if  len(password) < 6:
        print("password must be at least 6 cheracters. Try again ")

    elif not any(char.isdigit() for char in password)    
        print()
print("Password Accepted")