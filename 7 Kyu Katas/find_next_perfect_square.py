import math
def find_next_square(sq):
    """This function finds the next integral perfect square
    after the one passed as a parameter. Recall that an integral
    perfect square is an integer n such that sqrt(n) is also an integer.
    """
    res = math.sqrt(sq)
    if res.is_integer():
        return (res + 1)** 2
    return -1

print(find_next_square(121))
print(find_next_square(625))
print(find_next_square(319225))
print(find_next_square(15241383936))
print(find_next_square(155))
print(find_next_square(342786627))