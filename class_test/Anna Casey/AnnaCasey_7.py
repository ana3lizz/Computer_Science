a = input('Enter number A: ')
a = float(a)
b = input('Enter number B: ')
b = float(b)
if (a != b) and (a %2 != 0) and (b %2 != 0):
    print('A and B are different and are odd')
elif (a != b) and (a %2 == 0) and (b %2 ==0):
    print('A and B are different and are even')
else:
    print('Doesnt matter')