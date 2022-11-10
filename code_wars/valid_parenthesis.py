# create a function that, given an input string, returns a bolean whether parenthesis in that string are valid. given input y(3(p)p(3)r)s returns TRUE. given n(0(p)3 returns FALSE. given n0)(t(0)k returns FALSE

def is_still_valid(ope,clo):
    #making sure there are never more closed parenthesis than open ones
    if ope < clo:
        return False

def input_string(input):
    opened = 0
    closed = 0
    par_closed = True #starting with everything being ok
    for i in input:
        if i == "(":
            opened += 1
            #making sure that everytime we find a parenthesis we change the status of par_closed
            if par_closed == True:
                par_closed = False
            else:
                par_closed = True
        elif i == ")":
            closed += 1
            #making sure that everytime we find a parenthesis we change the status of par_closed
            if par_closed == False:
                par_closed = True
            else:
                par_closed = False
        if is_still_valid(opened,closed) == False:
            return False
    return par_closed

print(input_string("y(3(p)p(3)r)s"))
print(input_string("n(0(p)3"))
print(input_string("n0)(t(0)k"))
print(input_string("ll)ko(as"))
