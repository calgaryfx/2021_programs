# Write a function that suttters a word as if someone is struggling to read it.
# The first two letters are repeated twice with an ellipsis ... and space after
# each, and then the word is pronounced with a question mark ?.
def stutter(word):
    return ((word[:2] + "... ") * 2 + word + "?")

word = stutter("incredible")
print(word)

word = stutter("enthusiastic")
print(word)

word = stutter("outstanding")
print(word)
