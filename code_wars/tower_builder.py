# Build Tower
# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

# For example, a tower with 3 floors looks like this:

# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]
# And a tower with 6 floors looks like this:

# [
#   "     *     ", 
#   "    ***    ", 
#   "   *****   ", 
#   "  *******  ", 
#   " ********* ", 
#   "***********"
# ]


def tower_builder(n):
    tower = []
    i = 0
    while len(tower)<n:
        tower.append(f"{(n-i-1)*' '}{i*'*'}*{i*'*'}{(n-i-1)*' '}")
        i += 1
    return tower

print(tower_builder(1))
print(tower_builder(2))
print(tower_builder(3))
print(tower_builder(4))
print(tower_builder(5))

# def tower_builder(n):
#     return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]