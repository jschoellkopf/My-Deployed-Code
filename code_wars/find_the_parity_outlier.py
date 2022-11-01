def find_outlier(integers):
    even_nums = [i for i in integers if i % 2 == 0]
    odd_nums = [i for i in integers if i % 2 == 1]
    return even_nums[0] if len(even_nums) == 1 else odd_nums[0]

print(find_outlier([3, 2, 4, 6, 8, 10, 12]))
print(find_outlier([2, 4, 6, 8, 10, 12, 5, 14]))
print(find_outlier([2, 4, 6, 8, 10, 12, 7]))
print(find_outlier([3, 5, 7, 9, 11, 0]))
print(find_outlier([6, 3, 5, 7, 9, 11]))
print(find_outlier([3, 5, 7, 9, 8, 11]))

# def find_outlier(integers):
#     if integers[0] % 2 == 0:
#         if integers[1] % 2 == 1 and integers[2] % 2 == 1:
#             return integers[0]
#         for i in integers:
#             if i % 2 != 0:
#                 return i
#     else:
#         if integers[1] % 2 == 0 and integers[2] % 2 == 0:
#             return integers[0]
#         for i in integers:
#             if i % 2 == 0:
#                 return i
        

# def find_outlier(integers):
#     list_even = []
#     list_odd = []
#     for i in integers:
#         if i % 2 == 0:
#             list_even.append(i)
#         else:
#             list_odd.append(i)
#     if len(list_even) == 1:
#         return list_even[0]
#     else:
#         return list_odd[0]
