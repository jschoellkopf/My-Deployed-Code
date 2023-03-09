
# def order(sentence):
#     sentence = sentence.split()
#     result = [''] * len(sentence)
#     for i in sentence:
#         for x in i:
#             try:
#                 a = int(x)
#                 print(x)
#                 result[a-1] = i
#             except ValueError:
#                 pass
#     return " ".join(result)


def order(sentence):
    sentence = sentence.split()
    # getting array ready to receive the words in right order, so that we can use indecex
    result = [''] * len(sentence)
    
    # looping through words
    for i in sentence:

        # looping through each letter
        for x in i:

            # checking if character is a number and using that number as an index for the word it is contained in
            if x.isdigit(): 
                a = int(x)
                result[a-1] = i
                
    return " ".join(result)


print(order("is2 Thi1s T4est 3a"))
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"