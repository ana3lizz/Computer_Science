num = input('Guess a number from 1-10:')
num = float(num)
secret == 8.00
if num == secret:
    print('Bingo! Correct answer')
elif num == secret - 1 or num == secret + 1:
    print('Close enough to the correct answer.')
else:
    print('NO')
