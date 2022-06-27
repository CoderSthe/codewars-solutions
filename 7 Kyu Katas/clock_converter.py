# Your task is to write a function which returns
# the time since midnight in milliseconds.

def past(h, m, s):
    milliseconds = 0
    milliseconds +=(h *3600000)
    milliseconds +=(m * 60000)
    milliseconds +=(s * 1000)
    
    return milliseconds

print(past(1,1,1))