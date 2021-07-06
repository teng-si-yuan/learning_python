def highest_and_lowest_number(yangmiemie):
	y = 0
	z = 100000000
	if len(yangmiemie) == 0:
		return
	if len(yangmiemie) == 1:
		yangmiemie[0]
		return(yangmiemie[0], yangmiemie[0])
	for x in yangmiemie:
		if y < x:
			y = x
		if z > x:
			z = x
	return(y, z)

yangmiemie = [2, 4]
print(highest_and_lowest_number(yangmiemie))