# Create a function that takes an angle in radians and returns the corresponding
# angle in degrees rounded to one decimal place
from math import pi

def radians_to_degrees(rad):
    degree = (rad * 180) / pi
    degree = round(degree, 1)
    return degree

degrees = radians_to_degrees(1)
print(degrees)

degrees = radians_to_degrees(20)
print(degrees)

degrees = radians_to_degrees(50)
print(degrees)
