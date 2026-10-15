grade = input('Enter your grade: ')
grade = float(grade)
if grade >= 90:
    print('You got an A')
elif grade >= 80:
    if grade >= 85:
        print('You got a B+')
    else:
        print('You got a B')
elif grade >= 70:
    if grade >= 75:
        print('You got a C+')
    else:
        print('You got a C')
elif grade >= 65:
        print('You got a D+')
else:
    print('You got a D')