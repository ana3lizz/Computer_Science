sales = input('Enter your monthly sales: ')
sales = float(sales)
if sales >= 40000:
    com = (sales * 0.15)
else:
    com = (sales * 0.05)
print('Your monthly commision is', com)