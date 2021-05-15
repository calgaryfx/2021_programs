# Given an n-sided regular polygon n, return the total sum of internal angles
# in degrees.
def sum_polygon(n):
    angle_sum = (n - 2) * 180
    return angle_sum

a = sum_polygon(6)
print(a)
