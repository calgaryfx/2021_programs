# Count points for a basketball game. Count the 3 pointers and 2 pointers, return
# the total points.
def points(twopointers, threepointers):
    return (twopointers * 2) + (threepointers * 3)

a = points(1, 1)
print(a)

a = points(7, 5)
print(a)

a = points(38, 8)
print(a)
