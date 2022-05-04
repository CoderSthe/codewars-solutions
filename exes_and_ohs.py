# Check to see if a string has the same amount
# of 'x's and 'o's. The method must return a boolean
# and be case insensitive. The string can contain any char.

def xo(s):
    x_count = 0
    o_count = 0
    for char in s.lower():
        if char == 'x':
            x_count += 1
        if char == 'o':
            o_count += 1
    return x_count == o_count

print(xo('xxxoo'))