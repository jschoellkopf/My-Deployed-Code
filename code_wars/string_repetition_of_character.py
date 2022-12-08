def accum(s):
    new_str = ""
    count = 0
    cap_str = s.upper()
    for i in cap_str:
        new_str += i
        if count > 0:
            new_str += i.lower()*count
        count += 1
        if count < len(s):
            new_str += "-"
    return new_str

    print(accum("aKdLJPraeF"))

    