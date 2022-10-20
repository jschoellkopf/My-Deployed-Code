import string

def rot13(message):
    #doubling the alphabet so that there still is a character 13 places after "z"
    #otherwise, anything after the "m" (position 13) would give back an wrong letter or no letter if capital
    alphabet = list(string.ascii_lowercase + string.ascii_lowercase + string.ascii_uppercase + string.ascii_uppercase)
    code = ""
    for i in message:
        if not i.isalpha():
            code += i
        for l in range(len(alphabet)):
            if i == alphabet[l]:
                code += alphabet[l+13]
                break #make sure we stop once we found the letter, otherwise we'll get doubles
    return code

print(rot13("test"))

#could have used modulo instead of doubling the alphabet
#could have use .index
#interesting option: return message.translate(message.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))
