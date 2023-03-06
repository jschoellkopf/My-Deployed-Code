import math

def rSigma(num):
    if math.trunc(num) == 1:
        return num
    if num < 0:
        return 0
    return math.trunc(num) + rSigma(math.trunc(num-1))

print(rSigma(5))
print(rSigma(2.5))
print(rSigma(-1))

def factorial(num):
    if math.trunc(num) == 1:
        return num
    if num == 0:
        return 1
    return math.trunc(num) * factorial(math.trunc(num-1))

print(factorial(0))
print(factorial(3))
print(factorial(6.5))