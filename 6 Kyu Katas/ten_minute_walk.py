def is_valid_walk(walk):
    time, n, e, s, w = 0, 0, 0, 0, 0
    
    for direction in walk:
        time += 1
        if direction == 'n':
            n += 1
        elif direction == 's':
            s += 1
        elif direction == 'e':
            e += 1
        else:
            w += 1
    return (n == s and e == w and time == 10)
print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))
print(is_valid_walk(['w']))
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))