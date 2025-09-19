#what the fuck github, stop tweaking
#okay he stopped tweaking, but 10th push is too much for a single day.

#revision

# lenght = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
#
# perimeter = 2 * (lenght + width)
# area = lenght * width
# print(f"The perimeter of the rectangle is {perimeter} and the area of the rectangle is {area}")

# gpa = float(input("Declare, if you dare, the digits that measure your scholarly worth (0-5): "))
#
# if gpa > 5:
#     print("The council laughs at thy deceit!")
# elif gpa > 3.5:
#     print("Further trials yet await...")
# elif gpa < 3.5:
#     print("A tragic academic fate awaits you mortal!")

# Pay attention to the order of checks future Sova42!

import random

response = input("Would you like to sign my petition? (y/n): ")
if response == "y":
    print("Thanks!")
elif response == "n":
    reposnes = [
        "You're gonna sign this, or it will be your surviving family members",
        "You gotta be fucking kidding me",
        "You're gonna sign this petition or I'll follow you home and kill your dog"
    ]
    print(random.choice(reposnes))
else: print("fuck you, retarded piece of shit! type in fucking either letter n or y")