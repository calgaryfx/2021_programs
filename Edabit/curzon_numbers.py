# # Establish if a given integer num is a curzon number. If 1 plus 2 elevated to
# num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon
# number. Given a non-negative integer num, implement a function that returns
# True if num is a Curzon number, of False otherwise.
def is_curzon(num):
    return (2 ** num + 1) % (2 * num + 1) == 0
    
x = is_curzon(5)
print(x)

x = is_curzon(10)
print(x)

x = is_curzon(14)
print(x)
