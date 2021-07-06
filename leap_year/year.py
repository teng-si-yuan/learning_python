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
# print(is_leap_year(2100))

# x = 2000
# if x % 4 == 0:
#     if x % 400 == 0:
#         print("400 years")
#         print(True)
#     elif x % 100 == 0:
#         print("century")
#         print(False)
#     else:
#         print("Nowmal leap year")
# if x % 4 != 0:
#     print(False)




