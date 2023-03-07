def stock_list(lst, categories):
    if not lst or not categories:
        return ""
    sums = {c: 0 for c in categories}
    for code in lst:
        print(code[0])
        cat = code[0]
        if cat in categories:
            qty = int(code.split()[1])
            sums[cat] += qty
    return " - ".join(f"({c} : {sums[c]})" for c in categories)
    # result = []
    # for i in categories:
    #     result.append(f"({i} : {sums[i]})")
    # return = " - ".join(result)
    # 4 LINES INSTEAD OF ONE

b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B", "C", "D"]
stock_list(b, c)
