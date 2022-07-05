def summation(num):
    """This function finds the summation of every number
    from 1 to num. The number will always be a positive
    integer greater than 0."""

    summation = 0
    for i in range(1, num + 1):
        summation += i
    return summation

print(summation(1))
print(summation(8))
print(summation(22))
print(summation(100))
print(summation(213))