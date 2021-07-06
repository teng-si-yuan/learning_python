def highest_and_lowest_number(number_array):
	y = 0
	z = 100000000
	if len(number_array) == 0:
		return
	if len(number_array) == 1:
		number_array[0]
		return(number_array[0], number_array[0])
	for x in number_array:
		if y < x:
			y = x
		if z > x:
			z = x
	return(y, z)

number_array = [2, 4]
print(highest_and_lowest_number(number_array))