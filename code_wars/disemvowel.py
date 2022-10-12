from cgitb import text


# def disemvowel(string_a):
#     return string_a.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","").replace("A","").replace("E","").replace("I","").replace("O","").replace("U","")

def disemvowel(text_string):
    for i in "aeiouAEIOU":
        text_string = text_string.replace(i,"")
    return text_string