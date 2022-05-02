# Given a non-negative integer, 3 for example, return a string
# with a murmur: "1 sheep...2 sheep...3 sheep...".
# Input will always be valid, i.e. no negative integers.

def count_sheep(n):
    new_str = ""
    for i in range(n):
        new_str += f"{i + 1} sheep..."
        
    return new_str

print(count_sheep(3))