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

triangle = [[1],[1,1]]
def pascal(n):
  if n == 1:
    print(triangle[0])
  else:
    row_number = 2
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      length = len(row_prev)+1
      for i in range(length):
        if i == 0:
          row.append(1)
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    for row in triangle:
      print(row)
