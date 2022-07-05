def min_max(lst):
    """This function returns both the minimum and maximum
    number of a given list."""
    res = []
    res.append(min(lst))
    res.append(max(lst))
    
    return res

print(min_max([1,2,3,4,5]))
print(min_max([2334454,5]))
print(min_max([1]))