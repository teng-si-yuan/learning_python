def string_to_integer(number_string):
	b = []
	result = number_string.split()
	for a in result:
		b.append(int(a))
	return(b)

def highest_and_lowest(number_string):
	number_array = string_to_integer(number_string)
	highest_and_lowest_string = highest_and_lowest_number(number_array)
	return(highest_and_lowest_string)

def highest_and_lowest_number(number_array):
	y = 0
	z = 100000000
	if len(number_array) == 0:
		return('')
	if len(number_array) == 1:
		return str(number_array[0]) + ' ' + str(number_array[0])
	for x in number_array:
		if y < x:
			y = x
		if z > x:
			z = x
	return str(y) + ' ' + str(z)