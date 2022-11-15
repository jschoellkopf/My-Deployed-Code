def solution(input):
    pairs = []
    if len(input) % 2 == 1:
        input += "_"
    for i in range(1,len(input),2):
        pairs.append(input[i-1]+input[i])
    return pairs