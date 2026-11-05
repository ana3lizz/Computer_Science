num1 = input('Enter a number:')
num1 = float(num1)
num2 = input('Enter a second number:')
num2 = float(num2)
if num1 > num2:
    print(f'The greater number of {num1} and {num2} is {num1}')
elif num2 > num1:
    print(f'The greater number of {num1} and {num2} is {num2}')
elif num1 == num2:
    print(f'{num1} and {num2} are equal in value.')