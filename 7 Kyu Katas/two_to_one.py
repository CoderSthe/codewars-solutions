def longest(a1, a2):
    res = ""
    for char in "".join(sorted(a1 + a2)):
        if char not in res:
            res += char
    return res

print(longest("aretheyhere", "yestheyarehere"))
print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))
print(longest("inmanylanguages", "theresapairoffunctions"))
a = "abcdefghijklmnopqrstuvwxyz"
print(longest(a, a))
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
print(longest(a, b))