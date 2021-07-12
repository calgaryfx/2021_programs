from die import Die

# Create a D6. D6 being six sided dice. D8 being 8 sided dice.
die = Die()

# Make some rolls, and store the results in a list.
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)
print("Number of rolls:", (len(results)))
