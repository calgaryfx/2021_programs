import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk(5_000)
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(16, 9.6), dpi=128)
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth=1, zorder=1)

# Emphasize the first and last points of the walk.
ax.scatter(0, 0, c='green', edgecolors='none', s=100, zorder=2)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
    s=100, zorder=2)

plt.show()
