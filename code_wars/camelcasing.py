def to_camel_case(text):
    new_text = ""
    if text == "":
        return text
    for i in range(len(text)):
        if text[i].isalpha():
            if not text[i-1].isalpha():
                new_text += text[i].upper()
            else:
                new_text += text[i]

    return new_text


text = "the great-Stealth_warrior"
print(to_camel_case(text))

# def to_camel_case(text):
#     return text[:1] + text.title()[1:].replace('_', '').replace('-', '')