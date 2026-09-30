year = input('enter your year:')
year = float(year)
month = input('enter your month:')

if month == ('february'):
    if (year %4 == 0) and (year %100 != 0) or ((year %4 == 0) and (year %100 == 0) and (year %400 == 0)):
        print('it has 29 days')
    else:
        print('it has 28 days')
   
elif month == ('april') or month == ('june') or month == ('september') or month == ('november'):
    print('it has 30 days')
else:
    print('it has 31 days')