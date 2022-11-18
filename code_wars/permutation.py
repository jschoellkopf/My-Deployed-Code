# Create a function that returns whether the second string is a permutation of the first. For example, given ("mister", "stimer"), return True. Given ("mister", "sister"), return False.

def is_permutation(word1,word2):
    if len(word1) != len(word2):
        return False
    
    for letter in word1:
        if letter not in word2:
            return False
    
    for letter in word2:
        if letter not in word1:
            return False
    return True

print(is_permutation("mister","sister"))
print(is_permutation("sister","mister"))
print(is_permutation("mister","stimer"))
print(is_permutation("mississipi", "pissim"))