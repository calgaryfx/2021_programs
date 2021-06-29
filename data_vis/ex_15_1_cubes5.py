# Plot the first five cubic numbers.
import matplotlib.pyplot as plt

x_values = range(1, 6)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='red', s=50)

# Set chart title and label axes.
ax.set_title("Cubed Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set the range for each axis.
ax.axis([0, 10, 0, 140])

plt.show()
