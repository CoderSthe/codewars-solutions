# Given two integers a and b, which can be positive or negative,
# find the sum of all the integers between and including them and
# return it. If the two numbers are equal return a or b.
# Note: a and b are not ordered!

def get_sum(a,b):
    total = 0
    if a == b:
        return a
    elif a > b:
        for i in range(b, a+1):
            total += i
    elif b > a:
        for i in range(a, b+1):
            total += i
    return total

print(get_sum(-1,2))