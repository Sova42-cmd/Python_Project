# dictionary = a collection of {key:value} pairs
#              ordered AND changable. NO duplicates.

# capitals = {"USA": "Washington",
#             "India": "New Delhi",
#             "Russia": "Moscow",
#             "Armenia": "Yerevan"}

# print(capitals.get("USA"))
# capitals.update({"Germany":"Berling"}) #adds new element
# capitals.update({"USA":"New York"}) #updates existing element
# capitals.pop("Russia") #removes selected element
# capitals.popitem() #removes last element
# capitals.clear() #removes everything.

# keys = capitals.keys() #return only keys
# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# for value in capitals.values():
#     print(value)
#
# items = capitals.items()
# print(items)
# works the same as
# for key, value in capitals.items():
#     print(f"The capital of {key} is – {value}")

# CONCESSION STAND PROGRAM!
# dictionary {key:value}

menu = {"soda(r)": 3.00,
        "soda(l)": 4.50,
        "popcorn(s)": 200.00,
        "popcorn(l)": 450.50,
        "coffee": 2.95,
        "iced tea": 3.25,}

cart = []
total = 0

print("–––––––––Menu–––––––––")
for key, value in menu.items():
    print(f"{key:5}: ${value:.2f}")
print("––––––––––––––––––––––")

while True:
    food = input("What would you like to buy? (enter q to exit): ").lower()
    if food == "q":
        print("Arrivederci!")
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("––––––––––Your order–––––––––––")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")