def highest_number(number_array):
	z = 100000000
	if len(number_array) == 0:
		return([])
	if len(number_array) == 1:
		return(number_array[0])
	for x in number_array:
		if z > x:
			z = x
	return(z)

def sort(unordered_array):
	result = []
	if len(unordered_array) == 0:
		return([])
	if len(unordered_array) == 1:
		return([unordered_array[0]])
	while len(unordered_array) >= 1:
		x = highest_number(unordered_array)
		result.append(x)
		unordered_array.remove(x)
		if len(unordered_array) == 0:
			break
	return(result)
