def find_short(s):
    res = list(map(len, s.split()))
    l = res[0]
    for x in range(len(res)):
        if res[x] < l:
            l = res[x]
    return l 

    # def find_short(s):
    # return min(len(x) for x in s.split())