# Write a function that takes two integers 'hours', 'minutes', converts them to
# seconds, then adds them.
def convert(hours, minutes):
    return ((hours * 60) + minutes) * 60

seconds = convert(6, 7)
print(seconds)
