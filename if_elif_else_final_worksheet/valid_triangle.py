angle1 = input('enter your first angle:')
angle1 = float(angle1)
angle2 = input('enter your second angle:')
angle2 = float(angle2)
angle3 = input('enter your third angle:')
angle3 = float(angle3)
if angle1 == 0 or angle2 == 0 or angle3 == 0:
    print('this is not a valid triangle')
elif angle1 + angle2 + angle3 == 180:
    print('is a valid triangle')
else:
    print('this is not a valid triangle')