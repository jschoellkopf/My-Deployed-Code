# Task
# You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet).

# Input:

# If, you can read?

# Output:

# India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ?

# Note:

# There are preloaded dictionary you can use, named NATO
# The set of used punctuation is ,.!?.
# Punctuation should be kept in your return string, but spaces should not.
# Xray should not have a dash within.
# Every word and punctuation mark should be seperated by a space ' '.
# There should be no trailing whitespace

dictionary = {'A':'Alfa', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf',"H":"Hotel", 'I':'India', 'J':'Juliett', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'}

def to_nato(words):
    nato_words = []
    for char in words.upper():
        if char in dictionary:
            nato_words.append(dictionary[char])
        elif char != ' ':
            nato_words.append(char)
    return ' '.join(nato_words)

print(to_nato('If, you can read'))
print(to_nato('Did not see that coming'))
print(to_nato('.d?d!'))



# def to_nato(words):
#     return ' '.join(dictionary.get(char, char) for char in words.upper() if char != ' ')