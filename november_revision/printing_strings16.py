budget = input('Enter your budget:')
budget = float(budget)
season = input('Enter your season. (Summer or Winter):')
if budget <= 100:
    destination = 'Moldova'
    if season == 'Summer':
        percent = budget%30
        vac = 'Camp'
    elif season == 'Winter':
        percent = budget%70
        vac = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'Summer':
        percent = budget%40
        vac = 'Camp'
    elif season == 'Winter':
        percent = budget%80
        vac = 'Hotel'
elif budget > 1000:
    destination = 'Europe'
    percent = budget%90
    vac = 'Hotel'
    
print(f'Somewhere in {destination}')
print(destination, percent)