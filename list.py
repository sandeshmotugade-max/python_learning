import sys

List = [1, 2, 3.5, True, "Amit", "Amit"]
#print(List) # Output: [1, 2, 3.5, True, 'Amit', 'Amit'] 

# remove command
#List.remove("Amit") # This will remove the first occurrence of "Amit" from the list
#print(List) 

# append command
#List.append("Sandesh") # This will add "Sandesh" to the end of the list
#print(List)

## pop command
#List.pop(2) # This will remove the last element from the list
#print(List) # Output: [1, 2, 3.5, True, 'Amit']

# count command
#print(List.count("Amit")) # Output: 1, because "Amit" appears once in the list

## Reverse command
#List.reverse()  # This will reverse the list in place
#print(List)

# Sort command
#List.sort() # This will sort the list in ascending order, but it will raise an error because the list contains different data types (int, float, bool, str)
#print(List)

List_sort = ['sanglik','kupwad','miraj','pune','kolhapur']
List_sort.sort() # This will sort the list in ascending order
#print(List_sort) # Output: ['kolhapur','kupwad', 'miraj', 'pune', 'sangli']


#for city in List_sort:
 #   if city.__contains__('k'):
    #     print(city) # Output: kolhapur, kupwad, because they contain 'k' in their names
    # else:   
    #     print("No city contains 'k'")

## Min max command
# numbers = [5, 2, 9, 1, 7]
# print(min(numbers)) # Output: 1, because it is the smallest number in the list
# print(max(numbers)) # Output: 9, because it is the largest number in the list

## Merge Command
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# list1.extend(list2)
# print(list1) # Output: [1, 2, 3, 4, 5, 6]

#insert command
List.insert(2, "Sandesh") # This will insert "Sandesh" at index 2

#print(List) # Output: [1, 2, 'Sandesh', 3.5, True, 'Amit', 'Amit']

#print(sys.getsizeof(List)) # Output: 120, because the list contains 7 elements and each element takes 16 bytes of memory (for reference) + 8 bytes for the list object itself.)
 