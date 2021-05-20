# A vehicle needs 10 times the amount of fuel than the distance it travels.
# However, it must always carry a mininmum of 100 fuel before setting off.
# Create a function to calculate the amount of fuel it needs, given the distance.
# Distance > 0. Return 100 if calculated fuel is less than 100.
def calculate_fuel(n):  # 'n' is distance.
    n = int(n * 10)
    if n < 100:
        return 100
    else:
        return n


fuel = calculate_fuel(23.5)
print(fuel)
