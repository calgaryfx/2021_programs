# A snail goes up the stairs. Every step, he must go up the step, then go across
# to the next step. He wants to reach the top of the tower.
# Write a function that returns the distance the snail must travel to the top of
# the tower given the height and length of each step and the height of the tower.
def total_distance(height, length, tower):
    steps = tower / height
    return round((steps * length) + tower, 1)

a = total_distance(0.2, 0.4, 100.0)
print(a)

a = total_distance(0.3, 0.2, 25.0)
print(a)

a = total_distance(0.1, 0.1, 6.0)
print(a)
