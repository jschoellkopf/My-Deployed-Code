def kooka_counter(laughing):
    if not laughing:
        return 0
    count = 1
    last_h = laughing[0]
    for i in range(0,len(laughing),2):
        if last_h != laughing[i]:
            count += 1
            last_h = laughing[i]
    return count

print(kooka_counter("hahahahaha"))
print(kooka_counter("hahaHahaha"))
print(kooka_counter("hahahahahaHaHahaHa"))

# import re

# def kooka_counter(laughing):
#     return len(re.findall(r'(ha)+|(Ha)+',laughing))




# def kooka_counter(laughing):
#     return 0 if laughing == '' else laughing.count('Hah') + laughing.count('haH') + 1