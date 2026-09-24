cost = input('enter the cost of your bike:')
cost = float(cost)
if cost > 10000:
    tax = cost*.15
elif cost > 5000 and cost <= 10000:
    tax = cost*.10
else:
    tax = cost*.05
print('your road tax is', tax)