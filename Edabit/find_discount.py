# Create a function that takes two arguments: The original price and the discount
# percentage as integers and returns the final price after the discount.
def dis(price, discount):
    return round(price - (price * (discount / 100)), 2)

a = dis(1500, 50)
print(a)

a = dis(89, 20)
print(a)

a = dis(100, 75)
print(a)
