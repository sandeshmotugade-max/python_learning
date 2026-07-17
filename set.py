signal_color = {"red", "yellow","green"}
signal_other = {"orange", "yellow"}

# print(signal_color)
# print(signal_other)

# getall = signal_color| signal_other #pipe operator (|)
# print(getall)
# print(type(signal_color))

# getall = signal_color & signal_other #& operator
# print(getall)

# getall = signal_color - signal_other #- operator
# print(getall)
# getall = signal_other - signal_color
# print(getall)

print(signal_color.union(signal_other)) # pite = union operator
print(signal_color.intersection(signal_other)) #& = intersection operator
print(signal_color.difference(signal_other)) #- = difference operator

