def is_prime_number(the_number):
    y = 2
    while y < the_number:
        if the_number % y == 0:
            return(False)
        y = y + 1
    if the_number == y:
        return(True)
    if the_number == 0 or the_number == 1:
        return(False)

the_number = 53
print(is_prime_number(the_number))
