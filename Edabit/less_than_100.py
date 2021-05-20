# Given two numbers, return True if the sum of both numbers is less than 100.
# Otherwise, return False.
def less_than_100(a, b):
    total = a + b
    if total < 100:
        return True
    else:
        return False

total = less_than_100(22, 15)
print(total)

total = less_than_100(83, 34)
print(total)

total = less_than_100(3, 77)
print(total)

# Could have been as simple as:
# def less_than_100(a, b):
#     return a + b < 100
