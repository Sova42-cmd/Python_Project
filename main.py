#Arithemtic & Math

#Augmented Assignment Operators
# friends = 10
# print(friends)

#instead of writing friends = friends + 1, write →
#friends += 1, or basically any other action +-*/

# friends *=5
# print(friends)
# friends /=2
# print(friends)
# powerOf = friends ** 4300
# print(friends)

# remainder = friends % 3
# print(remainder)

# x = 3.14
# y = 69
# z = -1

# result = round(x)
# result = abs(z)
# result = pow(x, 3)
# result = max(x,y,z)
# result = min(x,y,z)
#
# print(result)

# import math
#
# x = 9.1
#
# # print(math.pi)
# # print(math.e)
# # result = math.sqrt(x) square root.
# # result = math.ceil(x) rounds the number up.
# # result = math.floor(x) rounds the number down.
#
# print(result)

import math

# Exercise #1 Circle circumference calculation C = 2πr

# radius = float(input("Enter the radius of the circle: "))
# circumference = 2 * math.pi * radius
# print(f"The circumference of the circle is: {round(circumference, 2)}")
# #{round(circumference, 2)} → is responsible for rounding the answer to a given decimal place.

# Exercise #2 Circle area calculation A = πr^2

# radius = float(input("Enter radius: "))
#
# area = math.pi * pow(radius, 2)
# print(f"The area of the circle is {round(area, 2)}")

# Exercise #3 Right triangle hypotenuse calculation c = √a^2+b^2

firstPage = float(input("Enter lenght of first page: "))
secondPage = float(input("Enter lenght of second page: "))

hypostenuseLength = math.sqrt(pow(firstPage, 2) + pow(secondPage, 2))
print(f"Hypostenuse length: {hypostenuseLength}")



