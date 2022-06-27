def high_and_low(numbers):
    """This function takes a string of numbers and returns a string
    with the highest value and lowest value from the given string."""

    numbers = numbers.split(" ")
    int_num = []
    for char in numbers:
        int_num.append(int(char))
    highest = max(int_num)
    lowest = min(int_num)

    return str(highest) + " " + str(lowest)



print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
print(high_and_low("1 2 3"))