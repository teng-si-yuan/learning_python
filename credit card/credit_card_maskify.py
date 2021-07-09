def maskify(yangmiemie):
	z = 0
	y = len(yangmiemie)
	if y <= 4:
		return yangmiemie
	else:
		result = ""
		a = 1
		for x in yangmiemie:
			if a >= (y - 3):
				result = result + x
			else:
				result = result + "#"
			a = a + 1
		return(result)

yangmiemie = "4556364607935616"
print(maskify(yangmiemie))