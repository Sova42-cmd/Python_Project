# Quiz guessing game

questions = ("How many continents are there on Earth?",
             "Who painted the Mona Lisa?",
             "How many planets are in our solar system?",
             "Which planet in the solar system is the hottest?",
             "The center of a black hole is called the...")

options = (("A. 3", "B. 4", "C. 7", "D. 10"),
           ("A. Claude Monet", "B. Vincent van Gogh ", "C. Jimi Hendrix", "D. Leonardo da Vinci"),
           ("A. 8", "B. 7", "C. 14", "D. 9"),
           ("A. Mercury", "B. Venus", "C. Mars", "D. Earth"),
           ("A. Wormhole", "B. Singularity", "C. Event Horizon", "D. Eclipse"))

answers = ("c", "d", "a", "b", "b")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("––––––––––––––––––")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter you answer (a/b/c/d): ").lower()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print(f"Incorrect!")
    question_num += 1

print("––––––––––––––––––")
print("––––– Results –––––")
print("––––––––––––––––––")

print("Answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Your guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

