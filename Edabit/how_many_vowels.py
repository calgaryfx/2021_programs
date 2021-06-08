# Create a function that takes a string and returns the number (count) of vowels
# conatined within it.
def count_vowels(txt):
    return sum([1 for x in txt.lower() if x in 'aeiou'])


a = count_vowels("Celebration")
print(a)

a = count_vowels("Palm")
print(a)

a = count_vowels("Prediction")
print(a)
