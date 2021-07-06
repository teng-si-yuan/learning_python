def vowel_count(yangmiemie):
	y = 0
	for x in yangmiemie:
		if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
			y = y + 1
	return(y)

yangmiemie = "aeiou"
print(vowel_count(yangmiemie))