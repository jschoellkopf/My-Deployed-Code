def duplicate_count(text):
    text = text.lower() #kata sees duplicates regardless of capitalization
    count = 0
    for i in text:
        if text.count(i) > 1:
            text = text.replace(i,'')
            count += 1

    return count

print(duplicate_count("Indivisibilities"))