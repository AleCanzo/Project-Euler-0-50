import calendar

sum=0
for year in range(1901, 2001):
    for mon in range(1,13):
        for day in range(1,list(calendar.monthrange(year, mon))[1]+1):
            if calendar.weekday(year, mon, day) == 6 and day == 1:
                sum = sum + 1
print(sum)