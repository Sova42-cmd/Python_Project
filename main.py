# String methods

# name = input("What is your name? ")
# phone_number = input("What is your phone number?: ")

# result = len(name)
# result = name.find(" ")
# .find() locates when the selected symbol appears first.
# .rfind() does the same but reversed.
# result = name.rfind("a")
# .capitilize capitilizes only the FIRST letter
# name = name.capitalize()
# name = name.upper()
# .upper/lower() makes ALL the letters uppercase
# name = name.lower()
# .isdigit() returns either true or false, based on whether the input is digit or not
#   gives false with mixted inputs too – Sova42 – False
# name = name.isdigit()
# name = name.isalpha()
# .isalpha() check the input for alphabetical symbols, numbers/spaces – returns False
# phone_number = phone_number.replace(" ", "–")
# .replace() is the most important one!!!

# Many more strin methods can be found by – print(help(str))

# print(help(str))

# Exercise – validate user input
# 1. username is no more than 12 characthers.
# 2. username must not contain spaces.
# 3. username must not contain digits.

# username = input("Enter your username: ")
#
# if len(username) > 12:
#     print("Your username cannot be more than 12 characters.")
# elif not username.find (" ") == -1:
#     print("Your username cannot contain any spaces")
# elif not username.isalpha():
#     print("Your username cannot contain any digits")
# else:
#     print(f"Welcome {username}")

# String indexing = accessing elements of sequence using [] (indexing operator)
#                     [start : end : step]

card_number = "4321-1234-9010-0010"

# print(card_number[0]) only first digit.
# print(card_number[:4]) first 4 digits.
# print(card_number[5:9]) from 5th to 9th digits.
# print(card_number[9:]) from 9th to the end.
# print(card_number[-1]) only last digit.
# print(card_number[::2]) returns every second digit.
# print(card_number[::3]) returns every third digit.

# last_digits = card_number[15:]
# last_digits = card_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")

card_number = card_number[::-1]
# [::-1] reverses the order of whole credit card.
print(card_number)