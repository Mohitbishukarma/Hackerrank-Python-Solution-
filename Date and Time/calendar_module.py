import calendar as cal
month, day, year = list(map(int, input().strip().split(" ")))
print(cal.day_name[cal.weekday(year, month, day)].upper())
