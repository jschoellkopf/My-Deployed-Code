def count(s):
    count = {}
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    return count

# print(count('aba'))
# print(count('aaba'))
print(count('ababba'))
# print(count(''))



# from collections import Counter

# def count(string):
#     return Counter(string)



# def count(string):
#     return {i: string.count(i) for i in string}



# def getCount(s):
#     return sum(c in 'aeiou' for c in s)