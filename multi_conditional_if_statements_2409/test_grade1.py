percent = input('enter your percentage:')
percent = float(percent)
if percent > 90:
    grade = 'A'
elif percent > 80 and percent <= 90:
    grade = 'B'
elif percent >= 60 and percent <= 80:
    grade = 'C'
else:
    grade = 'D'
print('you got a', grade)