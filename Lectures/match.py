
print("1. Pasta\n2. maggie\n3. coffie")
recipy = int(input("Enter recipe name: "))
match recipy:
    case 1:
        print("Boil water, add pasta and cook for 10 minutes.")
    case 2:
        print("Boil water, add maggie and cook for 5 minutes.")
    case 3:
        print("Boil water, add coffie powder and sugar, stir well and serve hot.")
    case _:
        print("Recipe not found.")