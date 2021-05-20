# Create a function that takes a number as its only argument and returns True if
# it's less than or equal to zero. Otherwise, return False.
def less_than_or_equal_to_zero(num):
    return num <= 0

num = less_than_or_equal_to_zero(5)
print(num)

num = less_than_or_equal_to_zero(0)
print(num)

num = less_than_or_equal_to_zero(-2)
print(num)
