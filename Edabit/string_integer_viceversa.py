# Write two functions:
# 1. 'to_int():' A function to convert a string to an integer.
# 2. 'to_str():' A function to convert a integer to a string.
def to_int(txt):
    return int(txt)

def to_str(num):
    return str(num)

text_to_int = to_int("77")
print(text_to_int + text_to_int)

num_to_text = to_str(77)
print(num_to_text + num_to_text)
