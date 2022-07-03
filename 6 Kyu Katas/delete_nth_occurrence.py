def delete_nth(order,max_e):
    """Given a list and a number, create a new list that contains each number of
    [list] at most n times, without reordering.
    EG. If the input number is 2, and the input list is [1,2,3,1,2,1,2,3],
    you take [1,2,3,1,2], drop the next [1,2] since this would lead to 
    1 and 2 being in the result 3 times, and then take 3, which
    leads to [1,2,3,1,2,3]"""
    
    new_list = []
    for num in order:
        if new_list.count(num) < max_e:
            new_list.append(num)
            
    return new_list

print(delete_nth([1,2,3,1,2,1,2,3], 2))