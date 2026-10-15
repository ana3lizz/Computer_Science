user = input('Enter your username: ')
if user == ('admin'):
    passw = input('Enter your password: ')
    if passw == ('admin123'):
        print('Access granted!')
    else:
        print('Incorrect password.')
else:
    print('Incorrect username.')