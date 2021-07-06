def triangular_number(x):
    i = 1
    y = 0
    while i <= x:
        y = y + i
        i = i + 1
    return(y)

def triangular_number_array(start):
    i = triangular_number(start - 1) + 1
    end = triangular_number(start)
    arr = []
    while i <= end:
        arr.append(i)
        i = i + 1
    return arr

# i = 1
# while i <= 100:
#     print(triangular_number_array(i))
#     i = i + 1

