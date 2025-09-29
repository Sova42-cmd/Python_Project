# Sphere formula program

# import math
#
# radius = float(input("Enter the radius of the sphere: "))
#
# volume = 4/3 * math.pi * pow(radius, 3)
#
# print(f"Volume of your sphere is {volume}")

import matplotlib.pyplot as plt
#
# x = [2024, 2025, 2026, 2027]
# y =[100, 20, 120, 400]
#
# plt.plot(x,y)
#
# plt.show()

games = ["Minecraft", "Ultrakill", "Team Fortress 2", "Kingdom Rush", ]
hours = [300, 100, 144, 80, ]  # numeric values

plt.bar(games, hours)  #games = string labels, hours = numbers
plt.title("Time Spent in My Favorite Games")
plt.xlabel("Games")
plt.ylabel("Hours Played")

plt.show()

