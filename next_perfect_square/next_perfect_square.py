def find_next_square(x):
    y = 1
    while y * y <= x:
        y = y + 1
    return y * y

print(find_next_square(121))
print(find_next_square(141))
print(find_next_square(114114114))
