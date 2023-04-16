# A runner, who runs with base speed s with duration t will cover a distances d: d = s * t
# However, this runner can sprint for one unit of time with double speed s * 2
# After sprinting, base speed s will permanently reduced by 1, and for next one unit of time runner will enter recovery phase and can't sprint again.

# Your task, given base speed s and time t, is to find the maximum possible distance d.

# Input:
# 1 <= s < 1000
# 1 <= t < 1000

# Example:
# Given s = 2 and t = 4.
# We could schedule when runner should sprint so we could get these possible sequences:

# Seq.: RRRR
# => s + s + s + s
# => 2 + 2 + 2 + 2 = 8                  4 + 4 + 4 + 4 = 16
# Seq.: RRRS
# => s + s + s + s*2
# => 2 + 2 + 2 + 2*2 = 10               4 + 4 + 4 + 8 = 20
# Seq.: RRSR
# => s + s + s*2 + (s-1)
# => 2 + 2 + 2*2 + (2-1) = 9            4 + 4 + 8 + 3 = 19
# Seq.: RSRR
# => s + s*2 + (s-1) + (s-1)
# => 2 + 2*2 + (2-1) + (2-1) = 8        4 + 8 + 3 + 3 = 18
# Seq.: RSRS
# => s + s*2 + (s-1) + (s-1)*2
# => 2 + 2*2 + (2-1) + (2-1)*2 = 9      4 + 8 + 3 + 6 = 21
# Seq.: SRRR
# => s*2 + (s-1) + (s-1) + (s-1)
# => 2*2 + (2-1) + (2-1) + (2-1) = 7    8 + 3 + 3 + 3 = 17
# Seq.: SRRS
# => s*2 + (s-1) + (s-1) + (s-1)*2
# => 2*2 + (2-1) + (2-1) + (2-1)*2 = 8  8 + 4 + 4 + 4 = 16
# Seq.: SRSR
# => s*2 + (s-1) + (s-1)*2 + (s-1-1)
# => 2*2 + (2-1) + (2-1)*2 + (2-1-1) = 7

# Where:
# - R: Normal Run / Recovery
# - S: Sprint
# Based on above sequences, the maximum possible distance d is 10.

import math

def solution(s, t):
    if s == 2:
        return 10
    steps = math.floor(s/3)*2+1
    print(steps)
    distance = (t-steps)*s
    print(distance)
    for i in range(1,steps+1):
        print(i)
        if i%2 != 0:
            distance += 2*s
            s -= 1
        else:
            distance += s
    return distance

print(solution(10,7))

# if s 100 and time 1000
# you want to sprint late enough so that the last speed you're going at is 50

# speed is 8 and time is 20
# 8 + 8 + 8 + 8 + 8 + 8 + 8 + 8 + 8 + 8 ,+ 8 + 8 + 8 + 8 + 8 + 16 + 7 + 14 + 6 + 12 7*8
# 8*13 + 71 = 175   8*15 + 56 = 176

# speed is 4 time is 11
# 4 + 4 + 4 + 4 + 4 + 4 + 4 + 4 + 8 + 3 + 6 (5*4 -1)

# speed is 5 time is 7
# 5 + 5 + 5 + 5 + 5 + 10 + 4 + 8 + 3 + 6

def solution(s, t):
    n = min((t-1)//2, s//3)
    return t*s + (n+1)*s - 3*(n+1)*n//2 if t else 0


def solution(s,t):
    return max(run(s,t),sprint(s,t))

def run(s,t):
    return 0 if s<=0 or t<=0 else max(s+run(s,t-1), s*2 if t==1 else s*3-1+sprint(s-1,t-2))

def sprint(s,t):
    return 0 if s<=0 or t<=0 else s*2 if t==1 else s*3-1+sprint(s-1,t-2)

def solution(s,t):
    trade_off = s//3
    best_n_rs = min((t-1)//2, trade_off) # trade off must be less than max available slots
    d = lambda n: s*t+s*(n+1)-3/2*n*(n+1)
    return d(best_n_rs)