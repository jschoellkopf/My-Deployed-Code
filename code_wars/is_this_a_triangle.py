# Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

# (In this case, all triangles must have surface greater than 0 to be accepted).

def is_triangle(a, b, c):
    return a+b>c and a+c>b and b+c>a

print(is_triangle(3,4,5))
print(is_triangle(3,3,5))

# def is_triangle(a, b, c):
#     a, b, c = sorted([a, b, c])
#     return a + b > c


# Build a function that will take the length of each side of a triangle and return if it's either an Equilateral, an Isosceles, a Scalene or an invalid triangle.

# It has to return a string with the type of triangle.
# For example:

# type_of_triangle(2, 2, 1) --> "Isosceles"

def type_of_triangle(a, b, c): 
    if not isinstance(a,int) or not isinstance(b,int) or not isinstance(c,int):
        return "Not a valid triangle"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a valid triangle"
    elif a == b == c:
        return "Equilateral"
    elif a == b or a == c or b == c:
        return "Isosceles"
    else:
        return "Scalene"
    

    # def type_of_triangle(a, b, c):
        # if not str(str(a)+str(b)+str(c)).isnumeric():
        #     return "Not a valid triangle"
        # a, b, c = sorted((a, b, c))
        # return "Not a valid triangle" if c >= a + b else "Equilateral" if a == b == c else "Isosceles" if a == b or b == c else "Scalene"