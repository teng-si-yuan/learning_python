def split_array(number_array, anchor):
    small = []
    big = []
    for y in number_array:
        if y < anchor:
            small.append(y)
        else:
            big.append(y)
    return(big,small)

the_array = [15,23,17,4,135]
small, big = split_array(the_array,99)
print(big)
print(small)



    