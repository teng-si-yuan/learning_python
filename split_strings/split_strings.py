def split_strings(yangmiemie):
	y = []
	a = ""
	for x in yangmiemie:
		a = a + x
		if len(a) == 2:
			y.append(a)
			a = ""
	if len(yangmiemie) % 2 == 1:
		y.append(yangmiemie[len(yangmiemie) - 1] + "_")
	return(y)

yangmiemie = "abcdefg"
print(split_strings(yangmiemie))
# if z % 2 == 0:
# 	a = a + x
# if z % 2 == 1:
# 	y.append(a)
# 	a = ""
# z = z + 1