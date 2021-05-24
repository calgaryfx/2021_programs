# Create a function that takes an integer and returns the factorial of that integer.
# That is, the integer multiplied by all the positive lower integers.
def factorial(num):
    return 1 if num < 2 else num * factorial(num - 1)

factor = factorial(3)
print(factor)

factor = factorial(5)
print(factor)

factor = factorial(13)
print(factor)
