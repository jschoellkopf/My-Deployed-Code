# The function receives a parameter n, which indicates the maximum number of points on one domino tile.
# calculate the max sum of points in the set without repeating tiles (2,1)/(1,2)

def dots_on_domino_bones(n):
    if n < 0:
        return -1
    sum = 0
    for i in range(n+1):
        for x in range(i,n+1):
            sum += x+i
    return sum


print(dots_on_domino_bones(2))