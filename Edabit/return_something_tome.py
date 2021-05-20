# Write a function that returns the string "something" joined with a space " "
# and the given argument 'a'.
def give_me_something(a):
    sentence = "something" + " " + a
    return sentence

a = give_me_something("is better than nothing")
print(a)

a = give_me_something("Bob Jane")
print(a)

a = give_me_something("something")
print(a)
