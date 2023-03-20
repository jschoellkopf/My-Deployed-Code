# Task:
# Given a list of integers, determine whether the sum of its elements is odd or even.

# Give your answer as a string matching "odd" or "even".

# If the input array is empty consider it as: [0] (array with a zero).

# Examples:
# Input: [0]
# Output: "even"

# Input: [0, 1, 4]
# Output: "odd"

# Input: [0, -1, -5]
# Output: "even"


def odd_or_even(arr):
    return "odd" if sum(arr)%2 != 0 else "even"

print(odd_or_even([0, 1, 2]))
print(odd_or_even([0, 1, 3]))
print(odd_or_even([1023, 1, 2]))