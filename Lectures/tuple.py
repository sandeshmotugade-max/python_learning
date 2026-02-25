
#tuple Declaration: tuple()
roll_nos = ("1", 2, 3.5, True, "Amit","Amit")

#roll_nos[0] = "2"   # Tuples are immutable, so this will raise an error

#print(type(roll_nos)) # Output: <class 'tuple'>

#print(" " in roll_nos) # Output: False, because "10" is not in the tuple using 'in' operator

color1 = ("Red","Blue", "Blue")
color2 = ("P","Q","R")

color1,color2= color2,color1  # Swapping values of color1 and color2

#print(color1) # Output: Green
#print(color2) # Output: Red


# Assiggn Values to the variables using tuple unpacking
stundent_info = ("John", 25, "A+", "Computer Science")
student_name, student_age, student_grade, student_major  = stundent_info

#print("Name:", student_name, "\n Age:", student_age)  # Output: Name: John Age: 25
#print("Grade:", student_grade) # Output: Grade: A+
#print("Major:", student_major) # Output: Major: Computer Science

#print(stundent_info)


## Internal working of tuple
color5, color6 = "Red", "Green"  # Tuple unpacking
print(color5) # Output: Red
print(color6) # Output: Green   

print(color2.count("Blue")) # Output: 2, because "Blue" appears twice in the tuple
