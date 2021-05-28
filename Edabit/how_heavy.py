# Given radius r and height h (in cm), calcualte the mass of a cylinder when it
# is filled with water and the cylinder itself doesn't weigh anything. The
# desired output should be given in kg and rounded to two decimal places.
from math import pi
def weight(r, h):
    return round(((pi * (r ** 2)) * h) * 0.001, 2)

a = weight(4, 10)
print(a)

a = weight(30, 60)
print(a)

a = weight(15, 10)
print(a)
