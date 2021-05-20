# Create a function to concatenate two integer lists.
def concat(lst1, lst2):
    return (lst1 + lst2)

numbers = concat([1, 3, 5], [2, 6, 8])
print(numbers)

numbers = concat([7, 8], [10, 9, 1, 1, 2])
print(numbers)

numbers = concat([4, 5, 1], [3, 3, 3, 3, 3])
print(numbers)
