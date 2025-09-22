import random

# number = random.randint(1,1000)
# print(number)

# low = 1
# high = 100
# number = random.randint(low, high)
# print(number)

# options = ("Rock", "Paper", "Scissors ")
#
# option = random.choice(options)
# print(option)

# cards = ["2", "3", "4,", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# random.shuffle(cards)
# print(cards)

#                       NUMBER GUESSING GAME!
#
# lowest_num = 1
# highest_num = 100
# answer = 42
# guesses = 0
# is_running = True

# print("Guessing game!")
# print(f"Select a number between {lowest_num} and {highest_num}")
#
# while is_running:
#     guess = input("Enter your guess!: ")
#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1
#         if guess < lowest_num or guess > highest_num:
#             print("That number is out of range!")
#             print(f"Select a number between {lowest_num} and {highest_num}")
#         elif guess < answer:
#             print("Too low! Pick again!")
#         elif guess > answer:
#             print("Too high! Pick again!")
#         else:
#             print(f"YESSSSIRRRR! the answer was {answer}")
#             print(f"Number of guesses it took: {guesses}")
#             is_running = False
#     else:
#         print("Invalid guess, guess a number!")

#                       ROCK PAPER SCISSORS GAME!!

# options = ("rock", "paper", "scissors")
# running = True
#
# while running:
#
#     player = None
#     computer = random.choice(options)
#
#     while player not in options:
#         player = input("Enter a choice (rock/paper/scissors): ")
#
#     print(f"Player: {player}")
#     print(f"Computer: {computer}")
#
#     if player == computer:
#         print("Tie!")
#     elif player == "rock" and computer == "scissors":
#         print("You won!")
#     elif player == "paper" and computer == "rock":
#         print("You won!")
#     elif player == "scissors" and computer == "paper":
#         print("You won!")
#     else:
#         print("You lost!")
#
#     # play_again = input("Play again? (y/n): ").lower()
#     # if not play_again == "y":
#     #     running = False
#
#     if not input("Play again? (y/n): ").lower() == "y":
#         running = False
#
# print("Thanks for playing! :>")

#                       DICE ROLLER PRORAM

# print("\u25cf \u250c \u2500 \u2510 \u2502 \u2514 \u2518")
#● ┌ ─ ┐ │ └ ┘



dice_art = {
  1: ("┌─────────┐",
      "│         │",
      "│    ●    │",
      "│         │",
      "└─────────┘"),
  2: ("┌─────────┐",
      "│  ●      │",
      "│         │",
      "│       ● │",
      "└─────────┘"),
  3: ("┌─────────┐",
      "│  ●      │",
      "│    ●    │",
      "│       ● │",
      "└─────────┘"),
  4: ("┌─────────┐",
      "│ ●     ● │",
      "│         │",
      "│ ●     ● │",
      "└─────────┘"),
  5: ("┌─────────┐",
      "│ ●     ● │",
      "│    ●    │",
      "│ ●     ● │",
      "└─────────┘"),
  6: ("┌─────────┐",
      "│ ●  ●  ● │",
      "│         │",
      "│ ●  ●  ● │",
      "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6 ))

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end=" ")
    print()

for die in dice:
    total += die
print(f"total is {total}")