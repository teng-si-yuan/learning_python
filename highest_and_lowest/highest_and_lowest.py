def string_to_array(number_string):
	number_array = []
	number_str_to_arr = number_string.split()
	for the_number in number_str_to_arr:
		number_array.append(int(the_number))
	return(number_array)

def highest_and_lowest(number_string):
	number_array = string_to_array(number_string)
	highest_and_lowest_string = highest_and_lowest_number(number_array)
	return(highest_and_lowest_string)

def highest_and_lowest_number(number_array):
	the_number_which_smaller = 0
	the_number_which_bigger = 100000000
	if len(number_array) == 0:
		return('')
	if len(number_array) == 1:
		return str(number_array[0]) + ' ' + str(number_array[0])
	for x in number_array:
		if the_number_which_smaller < x:
			the_number_which_smaller = x
		if the_number_which_bigger > x:
			the_number_which_bigger = x
	return str(the_number_which_smaller) + ' ' + str(the_number_which_bigger)