# Create a function that takes a list of numbers and returns the smallest number
# in the list.
def find_smallest_num(lst):
    return min(lst)

number = find_smallest_num([34, 15, 88, 2])
print(number)

number = find_smallest_num([34, -345, -1, 100])
print(number)

number = find_smallest_num([-76, 1.345, 1, 0])
print(number)

number = find_smallest_num([0.4356, 0.8795, 0.5435, -0.9999])
print(number)

number = find_smallest_num([7, 7, 7])
print(number)
