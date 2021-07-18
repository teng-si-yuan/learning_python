def age_of_days(birth_year, birth_month, birth_day, now_year, now_month, now_day):
	x = ((now_year - birth_year)* 365)
	y = month_days(birth_month, now_month)
	z = dates(birth_day, now_day)
	a = count_of_leap_year(birth_year, now_year, birth_month, now_month)
	return(x + y + z + a)

def month_days(birth_month, now_month):
	days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	y = 0
	i = birth_month
	if birth_month >= now_month:
		while i > now_month:
			i = i - 1
			# print(days_in_month[i - 1])
			y = y - days_in_month[i - 1]
	else:
		while i < now_month:
			# print(days_in_month[i - 1])
			y = y + days_in_month[i - 1]
			i = i + 1
	return(y)

def dates(birth_day, now_day):
	z = now_day - birth_day
	return(z)

def is_leap_year(year):
    y = False
    if year % 4 == 0:
        if year % 400 == 0:
            y = True
        elif year % 100 == 0:
            y = False
        else:
            y = True
    if year % 4 != 0:
        y = False
    return(y)

def count_of_leap_year(birth_year, now_year, birth_month, now_month):
	b = birth_year
	c = 0
	while b <= now_year:
		if is_leap_year(b):
			c = c + 1
		b = b + 1
	if is_leap_year(birth_year) and birth_month > 2:
		c = c - 1
	if is_leap_year(now_year) and now_month <= 2:
		c = c - 1
	return(c)

birth_year = 2021
birth_month = 7
birth_day = 1
now_year = 2022
now_month = 7
now_day  = 10