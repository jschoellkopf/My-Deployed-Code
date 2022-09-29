#1 Countdown
def count_down_from(x):
    count_down_list = []
    for i in range(x,-1,-1):
        count_down_list.append(i)
    return count_down_list
print(count_down_from(13))

#2 Print & Return
def print_return(x):
    print(x[0])
    return x[1]
print(print_return([3,7]))

#3 First Plus Length
def sum_first_length(x):
    return x[0] + len(x)
print(sum_first_length([12,6,4,3,7,8]))

#4 Values Greater Than Second
def val_greater_than_sec(x):
    new_list = []
    for i in x:
        print(i)
        if i > x[1]:
            new_list.append(i)
    if len(new_list) < 2:
        return False
    else:
        print(len(new_list))
        return new_list
print(val_greater_than_sec([6,9,13,5,46,7,23]))

#5 This Length, That Value
def length_value(a,b):
    new_list = []
    for x in range(a):
        new_list.append(b)
    return new_list
print(length_value(5,8))