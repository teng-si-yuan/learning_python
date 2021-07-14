def split_array(number_array, anchor):
    small = []
    big = []
    for y in number_array:
        if y < anchor:
            small.append(y)
        else:
            big.append(y)
    return(big,small)