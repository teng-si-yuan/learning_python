def days(year, month):
    result = []
    if year == 0:
        return(result)
    if month == 1:
        result.append('31')
    if year != 1 and year % 1000 != 0:
        if month == 2:
            if year % 4 == 0:
                result.append('29')
            else:
                result.append('28')
            if year == 1:
                result.append('29')
    if month == 3:
        result.append('31')
    if month == 4:
        result.append('30')
    if month == 5:
        result.append('31')
    if month == 6:
        result.append('30')
    if month == 7:
        result.append('31')
    if month == 8:
        result.append('31')
    if month == 9:
        result.append('30')
    if month == 10:
        result.append('31')
    if month == 11:
        result.append('30')
    if month == 12:
        result.append('31')
    if year == 1:
        result.append('29')
    if year % 1000 == 0:
        result.append('28')
    return(result)

print(days(0, 2))