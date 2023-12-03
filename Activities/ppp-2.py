def max_num (array):
    max = 0
    for integer in array:
        if integer > max:
            max = integer
    return max

def mult_list(lists):
    base = 1
    for integer in lists:
        base *= integer
    return base
def rev_string(string):
    return string[::-1]

def num_within(start,end,num):
    if start <= num <= end:
        return True
    else: 
        return False
