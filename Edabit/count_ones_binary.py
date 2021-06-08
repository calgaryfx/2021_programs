# Count the amount of ones in the binary representation of an integer. For
# example, since 12 is 1100 in binary, the reuturn value should be 2.
def count_ones(num):
    return bin(num).count('1')


a = count_ones(0)
print(a)

a = count_ones(100)
print(a)

a = count_ones(999)
print(a)
