age = input("Please enter your age: ")
bike_type = input("Please enter the type of bike you want (EV/Petrol): ")

if not age.isdigit():
    print("Please Enter number only")
elif int(age) >= 16 and int(age) < 18:
    print("You are eligible to EV bike.")
elif (int(age) >= 16 and int(age) <18) or bike_type.lower() == "ev":
    print("You are eligible to EV bike. or")
elif int(age) >= 18:
    print("You are eligible to Petrol bike.")
else:
    print("You are not eligible to Any.")