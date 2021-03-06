# Consider an array/list of sheep where some sheep
# may be missing from their place. We need a function
# that counts the number of sheep present in the array (true means present).

def count_sheeps(sheep):
    count = 0
    for present_sheep in sheep:
        if present_sheep:
            count += 1
    return count

array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]
print(count_sheeps(array1))