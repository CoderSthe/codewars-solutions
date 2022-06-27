# Square every digit of a number and concatenate them.
# For example, if we run 9119 through the function,
# 811181 will come out, because 92 is 81 and 12 is 1.

def square_digits(num):
    num_list = [int(x) for x in str(num)]
    new_str = ""
    
    for i in range(len(num_list)):
        new_str += str(num_list[i] ** 2)
        
    return int(new_str)

print(square_digits(9119))