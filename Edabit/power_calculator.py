# Create a function that takes voltage and current and returns the calculated
# power.
def circuit_power(voltage, current):
    power = voltage * current
    return power

circuit = circuit_power(480, 20)
print(circuit)
