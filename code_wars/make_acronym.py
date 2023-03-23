# Write function which takes a string and make an acronym of it.

# Rule of making acronym in this kata:

# split string to words by space char
# take every first letter from word in given string
# uppercase it
# join them toghether
# Eg:

# Code wars -> C, w -> C W -> CW
# Note: There will be at least two words in the given string!

def to_acronym(inp):
    return "".join(c[0].capitalize() for c in inp.split())

print(to_acronym("Code Wars"))
print(to_acronym("Water Closet"))
print(to_acronym("Portable Network Graphics"))
print(to_acronym("PHP: Hypertext Preprocessor"))
print(to_acronym("hyper text markup language"))