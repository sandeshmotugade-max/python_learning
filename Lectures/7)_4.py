correct_pin = 1234
attempts = 0

while attempts < 3:
    pin = int(input("Enter PIN: "))

    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        print("Incorrect PIN")
        attempts += 1
        print("Remaining Attempts:2") 

if attempts == 3:
    print("Card Blocked")