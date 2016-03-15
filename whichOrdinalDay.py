def whichOrdinalDay(month, day, year) :
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year in [1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024] : days_per_month[1] += 1
    ordinal_day = sum(days_per_month[0:month-1]) + day
    return ordinal_day

ordi = whichOrdinalDay(3, 1, 2012)

print ordi
