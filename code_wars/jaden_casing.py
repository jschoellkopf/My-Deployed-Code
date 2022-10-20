def to_jaden_case(string):
    # capitalize first letter of each word
    return " ".join(word[0].upper() + word[1:].lower() for word in string.split(" "))

print(to_jaden_case("Hi, how are you? It's a beautiful day."))

#even better: return " ".join(word.capitalize() for word in string.split(" "))