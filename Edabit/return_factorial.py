# Create a function that takes an integer and returns the factorial of that integer.
# That is, the integer multiplied by all the positive lower integers.
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact

factor = factorial(3)
print(factor)

factor = factorial(5)
print(factor)

factor = factorial(13)
print(factor)
