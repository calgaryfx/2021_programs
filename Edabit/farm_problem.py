# Count the legs among all the animals.
def animals(chickens, cows, pigs):
    total_legs = (chickens * 2) + (cows * 4) + (pigs * 4)
    return total_legs

legs = animals(5, 2, 8)
print(legs)
