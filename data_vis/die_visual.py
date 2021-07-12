from die import Die

# Create a D6. D6 being six sided dice. D8 being 8 sided dice.
die = Die()

# Make some rolls, and store the results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
print("Number of rolls:", (len(results)))
