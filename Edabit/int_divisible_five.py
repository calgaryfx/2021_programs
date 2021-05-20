# Create a function that returns True if an integer is evenly divisible by 5,
# and False otherwise.
def divisible_by_five(n):
    return n % 5 == 0

a = divisible_by_five(5)
print(a)

a = divisible_by_five(-55)
print(a)

a = divisible_by_five(37)
print(a)
