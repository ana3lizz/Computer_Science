year = input('enter your year:')
year = float(year)
if (year %4 == 0) and (year %100 != 0) or (year %4 == 0) and (year %100 == 0) and (year %400 == 0):
    print('it is a leap year')
elif (year %4 != 0):
    print('it is not a leap year')
else:
    print('it is not a leap year')