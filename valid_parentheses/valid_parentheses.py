def validate(input_string):
	if len(input_string) == 0:
		return(True)
	if len(input_string) % 2 == 1:
		return(False)
	i = 0
	j = 0
	while i < len(input_string):
		if input_string[i] == '(':
			j = j + 1
		if input_string[i] == ')':
			j = j - 1
		if j < 0:
			return(False)
		i = i + 1
	if j == 0:
		return(True)
	if j > 0:
		return(False)