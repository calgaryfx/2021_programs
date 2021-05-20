# Create a function that checks to see if two object arguments are equal to one
# another. Return True if the objects are equal, otherwise, return False.
def is_equal(obj_one, obj_two):
    if obj_one == obj_two:
        return True
    else:
        return False

obj_one = {
    "name": "Benny",
    "phone": "3325558745",
    "email": "benny@edabit.com",
}

obj_two = {
    "name": "Jason",
    "phone": "9853759720",
    "email": "jason@edabit.com",
}

# Object three is a test (copy of obj_one).
obj_three = {
    "name": "Benny",
    "phone": "3325558745",
    "email": "benny@edabit.com",
}
a = is_equal(obj_one, obj_two)
print(a)

a = is_equal(obj_one, obj_three)
print(a)
