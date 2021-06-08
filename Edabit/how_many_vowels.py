# Create a function that takes a string and returns the number (count) of vowels
# conatined within it.
def count_vowels(txt):
    count = 0
    word = txt.lower()
    vowels = ['a', 'e', 'i', 'o','u']
    for vowel in word:
        if vowel in vowels:
            count = count + 1
    return count


a = count_vowels("Celebration")
print(a)

a = count_vowels("Palm")
print(a)

a = count_vowels("Prediction")
print(a)
