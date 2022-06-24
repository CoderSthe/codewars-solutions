def remove_smallest(numbers):

    if numbers == []:
        return numbers

    smallest_num = min(numbers)
    numbers.remove(smallest_num)

    return numbers

numbers = [5,3,2,1,4]
print(remove_smallest(numbers))

# Option 2: Doing it without mutating the list
'''def remove_smallest(numbers):
    
    a = numbers[:]
    if a:
        a.remove(min(a))
        
    return a'''