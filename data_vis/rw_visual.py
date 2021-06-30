import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks with a while loop until 'n' is entered.
while True:
    # Make a random walk.
    rw = RandomWalk(50_000)     # Adding 50_000 here updates num_points def of
    rw.fill_walk()              # 5000 in random_walk.py

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(16, 9.6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolors='none', s=10)

    # Emphasize the first and last points of the walk.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=100)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
