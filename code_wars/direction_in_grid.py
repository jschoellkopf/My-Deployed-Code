# You're standing at the top left corner of an n × m grid and facing towards the right.

# Then you start walking one square at a time in the direction you are facing.

# If you reach the border of the grid or if the next square you are about to visit has already been visited, you turn right.

# You stop when all the squares in the grid are visited. What direction will you be facing when you stop?

# You can see the example of your long walk in the image below. The numbers denote the order in which you visit the cells.



# Given two integers n and m, denoting the number of rows and columns respectively, find out the direction you will be facing at the end.

# Output "L" for left, "R" for right, "U" for up, and "D" for down.

# Example:
# For n = 3, m = 3, the output should be "R".

# This example refers to the picture given in the description. At the end of your walk you will be standing in the middle of the grid facing right.

# Input/Output
# [input] integer n
# number of rows.

# 1 <= n <= 1000

# [input] integer m
# number of columns.

# 1 <= m <= 1000

# [output] a string
# The final direction.

def direction_in_grid(rows,cols):
    if rows == cols:
        if rows % 2 != 0:
            return "R"
        else:
            return "L"
    if rows > cols:
        if cols % 2 == 0:
            return "U"
        else:
            return "D"
    else:
        if rows % 2 == 0:
            return "L"
        else:
            return "R"
    return 0

print(direction_in_grid(1,1))
print(direction_in_grid(2,2))
print(direction_in_grid(2,3))
print(direction_in_grid(2,4))
print(direction_in_grid(3,1))
print(direction_in_grid(3,2))
print(direction_in_grid(3,3))
print(direction_in_grid(3,4))
print(direction_in_grid(3,5))
print(direction_in_grid(4,2))
print(direction_in_grid(4,3))
print(direction_in_grid(4,4))
print(direction_in_grid(4,5))
print(direction_in_grid(4,6))
print(direction_in_grid(5,4))
print(direction_in_grid(5,5))
print(direction_in_grid(5,6))
print(direction_in_grid(100,100),"L")

# def direction_in_grid(n, m):
#     return "LR"[n%2] if m >= n else "UD"[m%2]

# The function uses the modulo operator (%) to determine whether "n" or "m" is odd or even. If "n" is even, the modulo of "n" by 2 will be 0, and the function returns "LR"[0] which is equivalent to "L". If "n" is odd, the modulo of "n" by 2 will be 1, and the function returns "LR"[1] which is equivalent to "R". Similarly, if "m" is even, the function returns "UD"[0] which is equivalent to "U", and if "m" is odd, the function returns "UD"[1] which is equivalent to "D".