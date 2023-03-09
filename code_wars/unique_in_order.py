def unique_in_order(sequence):
    if not sequence:
        return []
    result =[sequence[0]]
    prev=sequence[0]
    for i in range(len(sequence)):
        if sequence[i] != prev:
            result.append(sequence[i])
        prev = sequence[i]
    return result

unique_in_order("")
unique_in_order("A")
unique_in_order("AABBADDAAASCCCSS")
unique_in_order("AASSDDDDcCCCcAAA")

# def unique_in_order(sequence):
#     if len(sequence) == 0:
#         return []
#     result = [sequence[0]]
#     for item in sequence[1:]:
#         if item != result[-1]:
#             result.append(item)
#     return result
