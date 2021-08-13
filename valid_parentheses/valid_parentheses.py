def validate(input_string):
	if len(input_string) == 0:
		return(True)
	if len(input_string) % 2 == 1:
		return(False)