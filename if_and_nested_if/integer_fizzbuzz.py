number = input('Enter an integer number:')
number = float(number)
if number %5 == 0 and number %3 == 0:
    print('FizzBuzz')
elif number %5 == 0:
    print('fizz')
elif number %3 == 0:
    print('buzz')
