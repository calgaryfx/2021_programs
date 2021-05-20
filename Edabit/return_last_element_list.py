# Create a function that accepts a list and returns the last item in the list.
# The list can be either homogenous or heterogenous.
def get_last_item(lst):
    return lst[-1]

a = get_last_item([1, 2, 3])
print(a)

a = get_last_item(["cat", "dog", "duck"])
print(a)

a = get_last_item([True, False, True])
print(a)

a = get_last_item([7, 'string', False])
print(a)

# return lst.pop() is also good.
