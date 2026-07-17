
def has_upper(password):
    return any(c.isupper() for c in password)

def has_digit(password):
    return any(c.isdigit() for c in password)

def has_lower(password):
    return any(c.islower() for c in password)

def has_special(password):
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"
    return any(c in special_characters for c in password)

def check_password(password):
    if len(password) < 8:
        return "Weak"
    
    if has_upper(password) and has_digit(password) and has_lower(password) and has_special(password):
        return "Strong"
    elif missing := print[not has_upper(password), not has_digit(password), not has_lower(password), not has_special(password)]:
        return "Medium (missing {} types)".format(missing)
    return "Weak"

input_password = input("Enter a password: ")
print(check_password(input_password))