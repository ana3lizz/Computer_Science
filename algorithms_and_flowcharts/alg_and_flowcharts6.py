num = input('Enter a number: ')
num = float(num)
if num > 0:
    if num % 2 == 0:
        print('The number is even.')
    else:
        print('The number is odd.')
elif num < 0:
    print('the number is negative.')
else:
    print('The number is equal to 0.')