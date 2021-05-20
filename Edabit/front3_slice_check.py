# Create a function that takes a string; the front is the first three characters
# of the string. If the string is less than three characters, the front is whatever
# is there. Return a new string, which is three copies of the front.
def front3(txt):
    return (txt[:3]) * 3

text = front3("Python")
print(text)

text = front3("Cucumber")
print(text)

text = front3("bioshock")
print(text)
