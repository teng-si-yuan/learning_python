from prime import is_prime_number
def prime_zhi_yin_zi(the_number):
    i = 1
    x = []
    while i <= the_number:
        if the_number % i == 0 and is_prime_number(i):
            x.append(i)
        i = i + 1
    return(x)
print(prime_zhi_yin_zi(200))
