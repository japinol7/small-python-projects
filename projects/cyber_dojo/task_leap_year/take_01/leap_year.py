def leap_year(year):
    if year < 1:
        return False

    if year % 400 == 0:
        return True
    if year % 4 == 0:
        return not (year % 100 == 0)
    return False
