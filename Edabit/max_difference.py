# Given a list of integers, return the difference between the largest and smallest
# integers in the list.
def difference(nums):
    return max(nums) - min(nums)

a = difference([10, 15, 20, 2, 10, 6])
print(a)

a = difference([-3, 4, -9, -1, -2, 15])
print(a)

a = difference([4, 17, 12, 2, 10, 2])
print(a)
