# Create a function that takes two numbers and a mathematical operator +, -, /,
# * and will perform a calculation with the given numbers.
def calculator(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Can't divide by 0!"
        else:
            return num1 / num2

a = calculator(2, "+", 2)
print(a)

a = calculator(2, "*", 2)
print(a)

a = calculator(2, "/", 0)
print(a)
