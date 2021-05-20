# Create a function that takes a name and returns a greeting in the form of a
# string.
def hello_name(name):
    return "Hello " + name + "!"

a = hello_name("Gerald")
print(a)

a = hello_name("Tiffany")
print(a)

a = hello_name("Ed")
print(a)


# This should have worked, Edabit is behind on 'f' strings.
# def hello_name(name):
#    return f"Hello {name}!"
