def is_all_negative(number_array):
	for x in number_array:
		if x >= 0:
			return(False)
	return(True)

def is_all_positive(number_array):
	for x in number_array:
		if x <= 0:
			return(False)
	return(True)

def array_sum(number_array):
	y = 0
	for x in number_array:
		y = y + x
	return(y)

def maximum_subarray_sum(integer_array):
	if len(integer_array) == 0:
		return(0, [])
	if len(integer_array) == 1:
		return(integer_array[0], integer_array)
	if is_all_positive(integer_array) == True:
		return(array_sum(integer_array), integer_array)
	if is_all_negative(integer_array) == True:
		return(0, [])
	if is_all_negative(integer_array) == False:
		return