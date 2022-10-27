def stray(arr):
    first_num = arr[0]
    first_num_arr = []
    second_num_arr = []
    for i in arr:
        if i == first_num:
            first_num_arr.append(i)
        else:
            second_num_arr.append(i)
    return first_num_arr[0] if len(first_num_arr) < len(second_num_arr) else second_num_arr[0]

# def stray(arr):
#     for x in arr:
#         if arr.count(x) == 1:
#             return x