def is_all_negative(number_array)
	for x in integer_array:
		if x >= 0:
			return(False)
	return(True)

def maximum_subarray_sum(integer_array):
	if len(integer_array) == 0:
		return(0, [])
	if len(integer_array) == 1:
		return(integer_array[0], integer_array)
	if is_all_negative(integer_array) == True:
		return(0, [])