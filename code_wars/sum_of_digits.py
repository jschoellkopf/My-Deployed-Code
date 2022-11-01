def digital_root(num):
    if num == 0:
        return num
    sum = 0
    num_string = str(num)
    switch = 0
    while sum > 9 or sum == 0:
        if switch == 0:    
            for i in num_string:
                sum += int(i)
                switch = 1
        else:
            sum2 = sum
            sum = 0
            for i in str(sum2):
                sum += int(i)

    return sum

print(digital_root(493193))

# def digital_root(n):
#     root = 0
#     for d in str(n):
#         root += int(d)
#     if len(str(root)) > 1:
#         root = digital_root(root)
#     return root