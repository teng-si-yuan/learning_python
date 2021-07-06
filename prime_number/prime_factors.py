def prime_factors(the_number):
  y = 1
  factors = []
  while y <= the_number:
    if the_number % y == 0:
      factors.append(y)
    y = y + 1
  if the_number == 0 or the_number == 1 or the_number == 2 or the_number == 3:
    return([])
  else:
    return(factors)
