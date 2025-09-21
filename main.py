# nested loops = a loop within another loop (outer, inner)
#                outer loop:
#                   inner loop:
# for y in range(1,4):
#     for x in range(1, 10):
#         print(x, end=" ")
#     print()

# rows = int(input("Enter the amount of rows: "))
# columns = int(input("Enter the amount of colums: "))
# symbol = input("Enter the symbol: ")
#
# for y in range (rows):
#     for x in range(columns):
#         print(symbol, end="")
#     print()

# collections = single "variable" used to store multiple values
    #   List = [] ordered and changable. Duplicates OK
    #   Set = {} unordered and immutable, but Add/Remove OK. NO duplicates.
    #   Tuple = () ordered and unchagnable. Dubplicates OK. FASTER
    #   Dictionary = ordered, mutable – for later.

# List
# albums = ["Bridges", "TWM", "Cryptic Writings", "Head Hunters"]

# print(albums[0]) #first element
# print(albums[3]) #4th element
# print(albums[:2]) #all elements until the 3rd one

# print("TWM" in albums) #returns True
# print("asd" in albums) #returns False

# albums.append("Octavarium") #adds an element to the end.
# albums.remove("TWM") #removes selected element.
# albums.insert(1, "Hot Rats") #insert element to prefered place.
# albums.sort() #sorts elements alphabetically.
# albums.reverse() #reverses current order of element.
# albums.clear() #removes all the elements.
# print(albums.count("TWM")) #counts how many of the same elements are there.

# print(albums)

# Set
# languages = {"Python", "JS", "Java", "C"}

# print(languages[0]) # → can't do this, because sets are unordered
# languages.remove("JS") # → acceptable
# languages.add("php") # → acceptable
# languages.pop() # → deleted first element (randomly)
#
# print(languages)

# Tuple
# planets = ("Mercury", "Venus", "Earth", "Mars", "Saturn")

#only two methods we have access to.

# print(planets.index("Venus")) #Venus's index is 1.
# print(planets.count("Earth")) #Only 1 Earth.

# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to purchase (enter q to exit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: "))
        foods.append(food)
        prices.append(price)

print("–––Your Cart–––")

for food in foods:
    print(food, end=", ")

for price in prices:
    total += price

print(f" – Your total is ${total}")

