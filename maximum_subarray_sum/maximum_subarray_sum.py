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
def sub_array(integer_array, start_index, last_index):
	result = []
	while start_index <= last_index:
		result.append(integer_array[start_index])
		start_index = start_index + 1
	return(result)
# print(sub_array([-1, 2, -3, 4], 0, 2))

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
		return(array_sum(loop_array(integer_array)), loop_array(integer_array))

def loop_array(integer_array):
	y = 0
	i = 0
	j = 0
	start_index = 0
	last_index = 0
	while j <= len(integer_array) - 1:
		if array_sum(sub_array(integer_array, i, j)) > y:
			y = array_sum(sub_array(integer_array, i, j))
			start_index = i
			last_index = j
		j = j + 1
	return(sub_array(integer_array, start_index, last_index))