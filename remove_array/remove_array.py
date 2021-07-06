def remove_array(yangmiemie,jigugu):
	y = []
	for x in yangmiemie:
		if x != jigugu:
			y.append(x)
	return(y)
yangmiemie = ['apple', 'banana', 'cherry']
jigugu = "banana"
print(remove_array(yangmiemie,jigugu))
