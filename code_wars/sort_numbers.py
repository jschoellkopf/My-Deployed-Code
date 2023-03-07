def solution(arr):
    if arr == None:
        return []
    if len(arr) <= 1:
        return arr
    n = len(arr)
    for i in range(n):
        # Find the minimum element
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
                
        # Swap the found minimum element with the first element
        arr[i], arr[min] = arr[min], arr[i]
    
    return arr

solution([1,2,3,5,3,7,10,4])

# def solution(nums):
#     return sorted(nums) if nums else []

# def solution(nums):
#     try:
#         return sorted(nums)
#     except TypeError:
#         return []