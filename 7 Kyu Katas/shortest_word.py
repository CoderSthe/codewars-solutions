# Given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

def find_short(s):
    sen_list = s.split()
    
    shortest_len = len(sen_list[0])
    
    for word in sen_list:
        if len(word) < shortest_len:
            shortest_len = len(word)
            
    return shortest_len

print(find_short("Boku no Hero Academia"))