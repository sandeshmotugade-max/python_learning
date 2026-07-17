
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b 

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculate(operation, a, b):
    if operation == "add":
        return add(a, b)
    elif operation == "sub":
        return subtract(a, b)
    elif operation == "mul":
        return multiply(a, b)
    elif operation == "div":
        return divide(a, b)
    

print(f"calculate('add', 10, 5) = {calculate('add', 10, 5)}")
print(f"calculate('sub', 10, 5) = {calculate('sub', 10, 5)}")
print(f"calculate('mul', 10, 5) = {calculate('mul', 10, 5)}")
print(f"calculate('div', 10, 5) = {calculate('div', 10, 5)}")
