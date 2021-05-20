# Given a list of integers, determine whether the sum of its elements is even or
# odd. The Return value should be a string ("odd" or "even").
# If the input list is empty, consider it as a list with a zero ([0]).
def even_or_odd(lst):
    num = sum(lst)
    if (num % 2 != 0):
        return "odd"
    else:
        return "even"

a = even_or_odd([0])
print(a)

a = even_or_odd([1])
print(a)

a = even_or_odd([])
print(a)

a = even_or_odd([0, 1, 5])
print(a)

a = even_or_odd([333, -207, 999, 541, -3233])
print(a)
