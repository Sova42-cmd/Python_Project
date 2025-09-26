# Banking program

def show_balance(balance):
    print("–––––––––––––––––––––––––––")
    print(f"Your balance is ${balance: .2f}!")
    print("–––––––––––––––––––––––––––")


def deposit():
    print("–––––––––––––––––––––––––––")
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("–––––––––––––––––––––––––––––––")
        print("Can't deposit a negative amount.")
        print("–––––––––––––––––––––––––––––––")
        return 0
    else:
        print("––––––––––––––––––––––––")
        print(f"You deposited ${amount}")
        print("––––––––––––––––––––––––")
        return amount

def withdraw(balance):
    print("–––––––––––––––––––––––––––––––")
    amount = float(input("Enter an amount to be withdrawn: "))

    if amount > balance:
        print("––––––––––––––––––––––––")
        print("You ain't got money dawg :(")
        print("––––––––––––––––––––––––")
        return 0
    elif amount < 0:
        print("Amaount must be greater than 0")
        return 0
    else:
        print("––––––––––––––––––––––––")
        print(f"You withdrawn ${amount}")
        print("––––––––––––––––––––––––")
        return amount

def main():

    balance = 0
    is_running = True

    while is_running:
        print("Welcome to Banking program!")
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter an action (1/2/3/4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("––––––––––––––––––––––––––––")
            print("Not valid action, try again!")
            print("––––––––––––––––––––––––––––")

if __name__ == "__main__":
    main()