#1
int1 = input('Enter your first integer number:')
int1 = float(int1)
int2 = input('Enter your second integer number:')
int2 = float(int2)
final = int1*int2
print(final)
#2
num = input('Enter your numerator:')
num = float(num)
den = input('Enter your denominator:')
den = float(den)
per = num/den
print(per, '%')
#3
one = input('Enter your first number:')
one = float(one)
two = input('Enter your second number:')
two = float(two)
thr = input('Enter your third number:')
thr = float(thr)
fou = input('Enter your fourth number:')
fou = float(fou)
fiv = input('Enter your fifth number:')
fiv = float(fiv)
al = (one+two+thr+fou+fiv) / 5
print(al)
#4
#€57.50
#5
din = input('Enter the number of diners:')
din = float(din)
bill = input('Enter the total bill:')
bill = float(bill)
tip = input('Enter the tip as a percentage:')
tip = float(tip)
tipp = bill %15
total = bill + tipp
perp = total / din
print('Each person should pay', perp)