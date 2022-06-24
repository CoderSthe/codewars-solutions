def digitize(n):
    
    reversed_list = []
    str_n = str(n)[::-1]
    for char in str_n:
        reversed_list.append(int(char))
        
    return reversed_list

print(digitize(12345))