# Python very basic calculator
# my version

# firstNumber = float(input("Enter first number: "))
# secondNumber = float(input("Enter second number: "))
#
# operetor = str(input("What should we do dawg? → +,-,*,/: "))
#
# if operetor == "+":
#     print(firstNumber + secondNumber)
# elif operetor == "-":
#     print(firstNumber - secondNumber)
# elif operetor == "*":
#     print(firstNumber * secondNumber)
# elif operetor == "/":
#     print(firstNumber / secondNumber)

# yt version

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = str(input("Enter an operator (+ - * /) → "))

if operator == "+":
    result = num1 + num2
    print(round(result, 2))
elif operator == "-":
    result = num1 - num2
    print(round(result, 2))
elif operator == "*":
    result = num1 * num2
    print(round(result, 2))
elif operator == "/":
    result = num1 / num2
    print(round(result, 2))
else:
    print(f"Something went wrong, I can't {operator} your numbers.")

# yt's code is more detailed, I'll consider that in the future.



