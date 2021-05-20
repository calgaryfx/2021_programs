# Create a function that takes a list and returns the difference between the
# largest and smallest numbers.
def difference_max_min(lst):
    maximum = max(lst)
    minimum = min(lst)
    difference = (maximum - minimum)
    return difference

a = difference_max_min([10, 40, 1, 4, -10, -50, 32, 21])
print(a)

a = difference_max_min([44, 32, 86, 19])
print(a)
