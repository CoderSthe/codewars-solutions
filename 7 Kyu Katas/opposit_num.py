def opposite(number):
    if number < 0:
        return abs(number)
    else:
        return float(f"-{number}")

print(opposite(25.6))