# for loops = execute a block of code a fixed number of times.
#             you can iterate over a range, string, sequence, etc.
#
# for x in range(1,11):
#     print(x)
#same but reversed ↓
# for x in reversed(range(1,11)):→
#     print(x)
# print("Congrats!")
#if x == something, continue → skips
# for x in reversed(range(1,21)):
#     if x == 13:
#         continue
#     print(x)
# print("Congrats!")

# break → stops at assign value.
# for x in range(1,21):
#     if x == 13:
#         break
#     print(x)
# print("Congrats!")

# countdown timer program!

# time.sleep(3)
# print("Time's up!")
# time.sleep just a timer, does nothing for 3 sec, then prints

import time

# time.sleep(3)
# print("Time's up!")
# time.sleep just a timer, does nothing for 3 sec, then prints

my_time = int(input("Enter the time in seconds: "))

# for x in reversed(range(0, my_time)): another technique to reverse ↓
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1) #duration of each second

print("Time's up!")

# Tested in a different file whether this would work as a timer to shut down/sleep
# and it did in fact work for sleep with os module.


