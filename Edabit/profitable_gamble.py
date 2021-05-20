# Create a function that takes three arguments prob, prize, pay and returns
# True if prob * prize > pay; otherwise return False.
def profitable_gamble(prob, prize, pay):
    if prob * prize > pay:
        return True
    else:
        return False

a = profitable_gamble(0.2, 50, 9)
print(a)

a = profitable_gamble(0.9, 1, 2)
print(a)

a = profitable_gamble(0.9, 3, 2)
print(a)

# Shorter version line 4:
# return (prob * prize) > pay
