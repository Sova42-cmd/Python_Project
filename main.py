# Logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be true.
#                     and = both conditions must be true.
#                     not = inverts the conditions (not False, not True)

#or
# temp = 25
# is_raining = False
#
# if temp > 35 or temp < 10 or is_raining:
#     print("No picnic today, bad weather :(")
# else:
#     print("Picnic today!")

#and
# temp = -20
# is_sunny = True
#
# if 20 < temp < 50 and is_sunny:
#     print("Sunny weather! a perfect day for a picnic!")
# elif 8 < temp < 20 and is_sunny:
#     print("Rather cold, but sunny")
# elif -100 < temp < 8 and is_sunny:
#     print("Sunny... but real cold, it's probably winter")

#not
# temp = 0
# is_sunny = True

# if temp <= 5 and is_sunny:
#     print("Rather cold today, but sunny!")
# if 5 <= temp <= 16 and is_sunny:
#     print("Light cold, but sunny!")
# if 16 <= temp <= 24 and is_sunny:
#     print("Great weather today, sunny")
# if 24 <= temp <= 40 and is_sunny:
#     print("Getting hot already!, sunny")
# if 40 <= temp and is_sunny:
#     print("good luck surviving this heat!, sunny af")
# #now really not operator
# if temp <= 5 and not is_sunny:
#     print("Rather cold today, and cloud")
# if 5 <= temp <= 16 and not is_sunny:
#     print("Light cold, and cloudy!")
# if 16 <= temp <= 24 and not is_sunny:
#     print("Great weather today, but cloudy")
# if 24 <= temp <= 40 and not is_sunny:
#     print("Getting hot already, but cloudy!")
# if 40 <= temp and not is_sunny:
#     print("good luck surviving this heat!, somehow f*cking cloudy tho")

# conditional expression = A one-line shortcut for if-else statement (ternary expression)
#                            Print or assign one of two values based on condition
#                            X if condition else Y

num = 42
a = 100
b = 101
age = 19
temp = 21
user_role = "admin"
passkey = 1234
# print("postivie" if num > 0 else "negative")
# print("even" if num % 2 == 0 else "odd")
# print(a if a > b else "b is greater than a")
# print(a if a < b else "a is less than b")
# print(a if a == b else "a is not equal to b")
# status = "Big dawg" if age >=18 else "Tiny winny"
# weather = "Perfect" if 17 < temp < 22 else "meh"
# permission = "welcome capitan!" if user_role == "admin" else "permission denied"
# user_input = int(input("Enter the pin: "))
# print("Welcome Boss" if user_input == passkey else "Try again")


