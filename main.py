# List comprehension = A concise short way to create lists in Python.
#                      Compact and easier to read than traditional loops.
#                      [expression for value in iterable if condition]

# doubles = []
# for x in range(1,11):
#     doubles.append(x*2)
#
# print(doubles)

#instead, write with this syntax ↓
# [expression for value in iterable if condition]

doubles = [x*2 for x in range(1,11)] #same result
triples = [y*3 for y in range(1,11)]
squares = [pow(z, 2) for z in range(1,11)]

print(squares)
#
# fruits = ["orange", "apple", "peach", "grape"]
#
# fruits = [fruit.capitalize() for fruit in fruits]
# print(fruits)

numbers = [-10, -9, 1, 3, 6, -1, 42, 31, -99, 4, 7, 8, -5]

positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if not num % 2 ==0]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)


#MATCH-CASE statement (switch) = An alternative to using many 'elif' statements.
#                                Execute some code, if a value matches a code.
#                                Benefits: cleaner, and syntax is more readable.

def is_weekend(day):
    match day:
        case "Sun" | "Sat":
            return True
        case "Mon" | "Tue" | "Wed" | "Thu" | "Fri":
            return False
        case _:
            return False

print(is_weekend("Mon"))
