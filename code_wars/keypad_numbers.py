def computer_to_phone(numbers):
    result = []
    for i in numbers:
        if int(i) > 6:
            result.append(str(int(i)-6))
        elif int(i) < 4 and i != '0':
            result.append(str(int(i)+6))
        else:
            result.append(i)
    return "".join(result)

print(computer_to_phone('09124753558'))

# def computer_to_phone(numbers):
#     return numbers.translate(str.maketrans('123789', '789123'))

# def computer_to_phone(_n):
#     comp = "0789456123"
#     phone = "0123456789"
#     return ''.join([phone[comp.index(i)] for i in _n])