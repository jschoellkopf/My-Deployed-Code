# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# For example, the score of abad is 8 (1 + 2 + 1 + 4).

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.

def high(x):
    # CAN BE SUBSTITUTED BY USING ORD()-96
    # alpha = "abcdefghijklmnopqrstuvwxyz"
    # count = 1
    # d = {} #Empty dictionary to add values into
    # for i in alpha:
    #     d[i] = count
    #     count+=1  
    score = 0
    highest_score = 0
    winning_word = ''
    for word in x.split():
        for letter in word:
            score += (ord(letter)-96)
        if score > highest_score:
            highest_score = score
            winning_word = word
        score = 0
    return winning_word

print(high('man i need a taxi up to ubud'))
print(high('what time are we climbing up the volcano'))
print(high('take me to semynak'))
print(high('aa b'))
print(high('b aa'))
print(high('bb d'))
print(high('d bb'))
print(high("aaa b"))

# def high(x):
#     return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

# def high(x):
#     words=x.split(' ')
#     list = []
#     for i in words:
#         scores = [sum([ord(char) - 96 for char in i])]
#         list.append(scores)
#     return words[list.index(max(list))]

# def high(x):
#     highest_score = 0
#     for word in x.split(' '):
#         score = sum(ord(c)-96 for c in word)
#         if score > highest_score:
#             highest_score = score
#             highest_word = word
            
#     return highest_word