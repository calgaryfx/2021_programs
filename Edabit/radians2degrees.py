# Re-wrote for single return line.
from math import pi

def radians_to_degrees(rad):
    return round((rad * 180) / pi, 1)

degrees = radians_to_degrees(1)
print(degrees)

degrees = radians_to_degrees(20)
print(degrees)

degrees = radians_to_degrees(50)
print(degrees)
