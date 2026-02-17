

name = 'Vyankatesh'

print("length_of_name",len(name))

print(name[0:4])    # Sclice 

print(name[0:7:2])  # Skip Characters

print(name[::-1])   # Reverse

#print indext of 'a' in name
print(name.index('a',4,7)) # Output: 3, because 'a' is at index 3 in the substring "ankatesh"

for i in name:
    index = name.index(i)
    print(index) # Output: V y a n k a t e s h, because it will print each character in the name on a new line

