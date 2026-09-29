athlone = input('Are you living in Athlone? (Enter Y or N):')
if athlone == ('Y'):
    age = input('How old are you?:')
    age = float(age)
    if age >= 18:
        registered = input('Are you registered to vote? (Enter Y or N):')
        if registered == ('Y'):
            print('You are able to vote')
        else:
            print('You must register to vote')
    else:
        print('You must be 18 years old to vote')
else:
    print('You must live in Athlone to vote.')