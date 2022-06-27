def duplicate_count(text):
    """This function returns the number of characters in a given
    string that have duplicates.
    EG. aabbcde would return 2(a and b)."""
    count = 0
    text = text.lower()
    new_list = []
    
    for char in text:
        if char not in new_list:
            new_list.append(char)
        else:
            if new_list.count(char) == 1:
                count += 1
                new_list.append(char)
    return count


print(duplicate_count(""))
print(duplicate_count("abcde"))
print(duplicate_count("abcdeaa"))
print(duplicate_count("abcdeaB"))
print(duplicate_count("Indivisibilities"))