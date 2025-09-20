# Compound interest calculator

initBalance = 0
time = 0
rate = 0

while initBalance <= 0:
    initBalance = float(input("Enter your initial balance (in $): "))
    if initBalance <= 0:
        print("can't be negative or zero")
    # elif initBalance > 0:
        # print(f"Your initial balance is {initBalance}, confirm? (y/n): ")
    # elif initialBalance == "y":
    #     print(f"Your inital balance is {initBalance}")
    # elif initBalance == "n":
    #     initBalance = float((input("Enter your initial balance (in $): ")))
else:
    print(f"Your initial balance is {initBalance}")

while rate <= 0:
    rate = float(input("Enter rate of change in % (e.g. 30%): "))
    if rate <= 0:
        print("can't be negative or zero")
else:
    print(f"Your rate of change is {rate}")

while time <= 0:
    time = float(input("Enter number of time periods (in years): "))
    if time <= 0:
        print("can't be negative or zero")
else:
    print(f"in {time} years you'll have this much green ${round(initBalance * (pow((rate/100)+1, time)), 3)}")