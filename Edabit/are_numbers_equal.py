# Create a function that returns 'True' when 'num1' is equal to 'num2': otherwise
# return 'False'.
def is_same_num(num1, num2):
    if num1 == num2:
        return True
    else:
        return False

a = is_same_num(4, 8)
print(a)

a = is_same_num(2, 2)
print(a)

a = is_same_num(2, "2")
print(a)


# This was offered up as a shorter solution. I like it:
def test(numb1, numb2):
    return numb1 == numb2

b = test(4, 8)
print(b)

b = test(2, 2)
print(b)

b = test(2, "2")
print(b)
