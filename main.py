# KEYWORD ARGUMENTS = an argument preceded by an identifier.
#                      helps with readability.
#                      order of arguments doesn't matter.

# def velocity(distance, time):
#      print(f"Velocity equals to {distance/time}")
#
# velocity(time=20, distance=120)
#
# def attack(player, weapon, damage):
#     print(f"{player} attacks with {weapon}, dealing {damage} damage!")
#
# # Using keyword arguments
# attack(damage=25, player="Sova42", weapon="bow")
# attack(weapon="magic staff", damage=50, player="the Midnight") #order of arguments not relevant


# ARBITRARY ARGUMENTS
# *args = allows you to pass multiple non-key arguments.
# **kwargs = allows you to pass multiple keyword-arguments.
#         * unpakcing operator

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
#
# print(add(1,2,3,12,123,312,3123)) # tuples

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
#
# display_name("Doctor", "Freeeeeman...", "I realize this moment might not be the most convenient")

def print_address(**kwargs):
    # for key in kwargs.keys():
    #     print(key)
    # for value in kwargs.values():
    #     print(value)
    for key, value in kwargs.items():
        print(f"{key} –> {value}")

print_address(street="123 St.",
              city="Paris",
              zip=90128,
              apartment="321") # dictionary

