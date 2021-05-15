# There is a single operator in Python, capable of providing the remainder of
# a division operator. Two numbers are passed as parameters. The first parameter
# divided by the second paramater will have a remainder, possibly zero. Return
# the value.
def remainder(x, y):
    remains = x % y
    return remains

a = remainder(7, 3)
print(a)
