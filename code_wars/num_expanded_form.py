# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.

# If you liked this kata, check out part 2!!

def expanded_form(num):
    answer,num = [], str(num)
    for i in range(len(num)):
        if num[i] != '0':
            answer.append(f"{num[i]}{'0'*(len(num)-i-1)}")
    return " + ".join(answer)


# print(expanded_form(12));
# print(expanded_form(42));
print(expanded_form(70304));



# def expanded_form(num):
    # return ' + '.join(x + '0' * (len(str(num)) - y - 1) for y,x in enumerate(str(num)) if x != '0')

# >>> for count, value in enumerate(values):
# ...     print(count, value)
# ...
# 0 a
# 1 b
# 2 c