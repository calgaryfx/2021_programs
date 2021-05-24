# A tetrahedron is a pyramid with a triangular base and three sides. A tetrahedral
# number is a number of items within a tetrahedron.
# Create a function that takes an integer n and returns the nth tethrahedral number.
def tetra(n):
    return int((n * (n + 1) * (n + 2)) / 6)

a = tetra(2)
print(a)

a = tetra(5)
print(a)

a = tetra(6)
print(a)
