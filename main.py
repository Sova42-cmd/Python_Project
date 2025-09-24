# Membership operators = used to test whether a value or variable is found in a sequence.
#                        (stirng, list, tuple, set or dictionary)
#                        1. in
#                        2. not in

# STRING
# word = "apple"
#
# letter = input("Guess a letter of the word: ")
#
# if letter in word:
#     print(f"The letter: {letter} is int the word")
# else:
#     print(f"The letter: {letter}, isn't in the word")

#LIST (tuples and sets behave the same way)
# guitarists = {"Jimi Hendrix", "Guthrie Govan", "Brian May", "Steve Vai"}
#
# guitarist = input("Enter a name of famous guitarist: ")
#
# if guitarist in guitarists:
#     print(f"{guitarist} is on the list!")
# else:
#     print(f"{guitarist} is not on the list.")

#DICTIONARY
musicians = {"Guthrie Govan": "Guitarist",
             "Chopin": "Pianist",
             "Mike Portnoy": "Drummer",
             "Bob Marley": "Singer"}

musician = input("Enter the name of the musician: ")

if musician in musicians:
    print(f"{musician} is a {musicians[musician]}")
else:
    print(f"{musician} not on the list")

#PRACTICAL EXAMPLE
email = "steviewonder@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email, must contain '@' and '.'")
