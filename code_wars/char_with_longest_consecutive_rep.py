# For a given string s find the character c (or C) with longest consecutive repetition and return:

# (c, l)
# where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.

# For empty string return:

# ('', 0)
# Happy coding! :)

def longest_repetition(chars):
    if not chars:
        return ('', 0)
    max_char = chars[0]
    curr_char =chars[0]
    curr_len = 0
    max_len = 0
    for i in range(len(chars)):
        if chars[i] == curr_char:
            curr_len +=1
        else:
            if curr_len > max_len:
                max_len = curr_len
                max_char = curr_char
            curr_char = chars[i]
            curr_len=1
    if curr_len > max_len:
        max_len = curr_len
        max_char = curr_char
    return (max_char, max_len)

# print(longest_repetition("aaaabb"))
# print(longest_repetition("bbbaaabaaaa")),
print(longest_repetition("cbdeuuu900")),
# print(longest_repetition("abbbbb"))
# print(longest_repetition("aabb"))
# print(longest_repetition("ba"))
# print(longest_repetition(""))


# from itertools import groupby
# def longest_repetition(chars):
#   return max([(x, len(list(gp))) for x, gp in groupby(chars)], key = lambda x: x[1], default = ('', 0))