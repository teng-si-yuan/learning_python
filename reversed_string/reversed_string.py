def reversed_string(yangmiemie):
	x = 0
	y = ""
	while x > -len(yangmiemie):
		x = x - 1
		y = y + yangmiemie[x]
	return(y)

yangmiemie = "world"
print(reversed_string(yangmiemie))