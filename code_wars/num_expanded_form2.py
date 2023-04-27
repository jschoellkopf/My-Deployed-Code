# his is version 2 of my 'Write Number in Exanded Form' Kata.

# You will be given a number and you will need to return it as a string in expanded form :

# expanded form illustration

# For example:

# expanded_from(807.304); // Should return "800 + 7 + 3/10 + 4/1000"
# expanded_from(1.24); // should return "1 + 2/10 + 4/100"
# expanded_from(7.304); // should return "7 + 3/10 + 4/1000"
# expanded_from(0.04); // should return "4/100"

# def expanded_form(num):
#     answer = []
#     num = str(num)
#     decimal = False
#     decimal_idx = num.index(".")
    
#     for i in range(len(num)):
#         if num[i] != '0' and decimal == False:
#             if num[i] != ".":
#                 answer.append(f"{num[i]}{'0'*(len(num)-i-1-(len(num)-decimal_idx))}")
#             else:
#                 decimal = True

#         if num[i] != '0' and decimal == True and num[i] != ".":
#             answer.append(f"{num[i]}/1{'0'*(i-decimal_idx)}")

#     return " + ".join(answer)

def expanded_form(num):
    parts = str(num).split(".")
    return ' + '.join([x + '0' * (len(str(num)) - y - 1- str(num).index(".")) for y,x in enumerate(parts[0]) if x != '0']+[x + '/10'+'0' * y for y,x in enumerate(parts[1]) if x != '0'])

# print(expanded_form(12));
# print(expanded_form(42));
print(expanded_form(70304.7098));




# >>> for count, value in enumerate(values):
# ...     print(count, value)
# ...
# 0 a
# 1 b
# 2 c