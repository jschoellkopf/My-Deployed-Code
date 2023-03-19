
from math import ceil

def cantor(n : int) -> str:
    r   = ceil((-1 + (1+8*n)**.5) / 2)
    n  -= r * (r-1) >> 1
    n,d = (r+1-n,n) if r&1 else (n,r+1-n)
    return f'{ n }/{ d }'


# def cantor(n : int) -> str:
#     if n == 1:
#         return '1/1'
#     else:
#         k = 1
#         while n > k:
#             n -= k
#             k += 1
#             print(n,k)
#         if k % 2 == 0:
#             return str(n) + '/' + str(k-n+1)
#         else:
#             return str(k-n+1) + '/' + str(n)


# def cantor(n, a=1, b=1, index=1, stop = True, going_down = True):
#     print(a,b)
#     if index == n:
#         return f"{a}/{b}"
#     elif a == 1 and stop == True:
#             return cantor(n, a, b + 1, index + 1, stop = False, going_down=True)
#     elif a == 1 and going_down == False:
#             return cantor(n, a, b, index, stop = True, going_down=True)
#     elif b > 1 and going_down == True:
#             return cantor(n, a + 1, b - 1, index + 1, stop = False, going_down = True)
#     elif b == 1 and stop == True:
#             return cantor(n, a + 1, b, index + 1, stop = False, going_down=False)
#     elif b == 1 and going_down == True:
#             return cantor(n, a, b, index, stop = True, going_down=True)
#     elif a > 1 and going_down == False:
#             return cantor(n, a - 1, b + 1, index + 1, stop = False, going_down=False)



# def cantor(n : int) -> str:
#     sequence = []
#     a = 1
#     b = 1
#     sequence.append(f'{a}/{b}')
#     while len(sequence) < n:
#         if a == 1:
#             b += 1
#             sequence.append(f'{a}/{b}')
#             going_down = True
#         if going_down:
#             while b != 1:
#                 a += 1
#                 b -= 1
#                 sequence.append(f'{a}/{b}')
#             going_down = False
#         if b == 1:
#             a += 1
#             sequence.append(f'{a}/{b}')
#         if not going_down:
#             while a != 1:
#                 a -= 1
#                 b += 1
#                 sequence.append(f'{a}/{b}')
#             going_down == True
#     print(sequence)
#     return sequence[n-1]

# # 268435455
for i in range(10):
    print("i is",i, cantor(i))