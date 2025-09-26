# Python slot machine
import random

def spin_row():
    symbols = ["⭐️", "🍒", "♥️", "🔔", "🍋"]

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):

    print(" | ".join(row))
    print("             ")

def get_payout(row, bet):

    if row[0] == row[1] == row[2]:
        if row[0] == "🍋":
            return bet * 5
        elif row[0] == "🍒":
            return bet * 10
        elif row[0] == "♥️":
            return bet * 15
        elif row[0] == "🔔":
            return bet * 50
        elif row[0] == "⭐":
            return bet * 100
    return 0

def main():
    balance = 100

    print("––––––––––––––––––––––––")
    print("Welcome to Python Slots!")
    print("Symbols: ⭐️ 🍒 ♥️ 🔔 🍋")
    print("––––––––––––––––––––––––")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet: ")

        if not bet.isdigit():
            print("Invalid input, try again!")
            continue

        bet = int(bet)

        if bet > balance:
            print("Not enough money vro ;<")
            continue

        if bet <= 5:
            print("Spin it, coward. Time to man up")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)
        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}, Congrats!!")
        else:
            print("Sorry, you lost, better luck next time!")

        balance += payout

        play_again = input("Spin again? (y/n): ")

        if play_again != "y":
            break

    print("––––––––––––––––––––––––––––––––––––––––––––")
    print(f"Game over! Your final balance is ${balance}")
    print("––––––––––––––––––––––––––––––––––––––––––––")


if __name__ == "__main__":
    main()