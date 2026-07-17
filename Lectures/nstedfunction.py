
# Online Python

#Globa Scope
a=10
b= 2

#Syntax

######## function area ###########
def addition():
    c=20
    
    def sub_addition():
        d= 100
        return c + d
    
    total = sub_addition()
    print(total)
    return total

###############################


c_return_value = addition()
total = a+ b+ c_return_value

print(total)

