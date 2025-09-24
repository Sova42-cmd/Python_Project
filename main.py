# default arguments = A default value for certain parameters
#                     Default is used when that argument is omitted(not done)
#                     make your function more flexible, reduced number of arguments.
#                     1. positional
#                     2. Default
#                     3. keyword
#                     4. arbitrary

#. 1 POSITIONAL

def play_song(title, instrument, duration):
    print(f"Now playing '{title}' on {instrument} for {duration} minutes!")

# Using positional arguments
play_song("Banana Jazz", "guitar", 5)
play_song("Dreamscape", "piano", 7)


#. 2 DEFAULT

# def net_price(list_price, discount=0, tax=0.05):
#         return list_price * (1-discount) * (1+tax)
#
# print(net_price(500, 0.1))

# COUNT UP TIMER
#
# import time
#
# def counter(end, start=0): #default arguments come after non-default
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("Finished")
#
# counter(10)