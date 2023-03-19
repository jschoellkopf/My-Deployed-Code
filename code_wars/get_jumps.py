def get_jumps(cl, k):
    curr = cl[0]
    jumps = 0
    while True:
        jumps += 1
        next_idx = (cl.index(curr) + k) % len(cl)
        if next_idx == 0:
            next_idx = len(cl) - 1
        if cl[next_idx] == cl[0]:
            return jumps
        curr = cl[next_idx]

# print(get_jumps([1, 5, 7, 8, 9],1))
# print(get_jumps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11],3))
print(get_jumps([1, 5, 7, 8, 9], 1))
print(get_jumps([1, 5, 7, 8, 9], 2))
print(get_jumps([1, 5, 1], 2))
# print(get_jumps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11],3))

# from math import gcd

# def get_jumps(cycle_list, k):
#     l = len(cycle_list)
#     return l // gcd(l, k)


# import math

# def get_jumps(cycle_list, k):
#     return math.lcm(len(cycle_list), k) // k