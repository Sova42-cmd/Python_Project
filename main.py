# Typecasting = a process of converting a variable from one data type to another!
#str(), int(), float(), bool()
#especially useful for handling user input, since it's mainly str().

# name = "Sova42"
# experience = 17
# version = 42.24
# is_online = True

# print(type(is_online))
# print(type(version))

# version = int(version)
# print(version)

# experience = float(experience)
# print(experience)

# Could be used for entering a name/login/password
# name = bool(name)
# print(name)

# input () = A function that prompts the user to enter a data.
#            Returns the entered data as a string.

# name = input("What is your name?")
# print(f"Hello {name}!! :3")
#
# float = input("What is your exact GPA?")
# print(f"You dumbass nigga!")
#
# age = input("Anyway, how old are you?")
# #Use typecasting, since can't add int to str.
# #Or enclose an input with a typecast -> int(input("")) or bool(input("")) !
# age = int(age)
# age = age + 1
# print(f"You're going to be {age} years old next year!.")

#Exercise #1 – Rectangle area calculation

# lenght = float(input("What's the lenght of the rectangle?"))
# width = float(input("What's the width of the rectangle?"))
# area = lenght * width
#
# print(f"The area of the rectangle is → {area}")

#Exercise #2 - Shopping cart program

# item = input("What item would you like to purchase?")
# price = float(input("What's the price of your item?"))
# quantity = int(input("How many would you like to purchase?"))
#
# total = price * quantity
# print(f"Your total price is ${total}")

# Madlibs game – word game where create a story by filling in blanks with random words

# noun1 = input("Enter the first noun (thing): ")
# adjective1 = input("Enter the first adjective (description): ")
# noun2 = input("Enter the second noun (thing): ")
# adjective2 = input("Enter the second adjective (description): ")
# verb1 = input("Enter the a verb (action): ")
#
# print(f"I woke up in a strange place, probably in {noun1}.")
# print(f"After some time I heard a weird noise, seemed rahter {adjective1}.")
# print(f"It was {noun2} HIMSELF! pretty {adjective2}.")
# print(f"Consfused I started {verb1}, and woke up the second time. It was just a dream.")
