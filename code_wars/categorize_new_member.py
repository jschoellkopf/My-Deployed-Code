# To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

def open_or_senior(data):
    output = []
    for applicant in data:
        if applicant[0] >= 55 and applicant[1] > 7:
            output.append("Senior")
        else:
            output.append("Open")
    return output
print(open_or_senior([[45, 12],[55,21],[19, -2],[104, 20]]))
print(open_or_senior([[16, 23],[73,1],[56, 20],[1, -1]]))
