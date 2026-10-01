rain = input('Is it raining?: ')
if (rain == ('yes')) or (rain == ('Yes')) or (rain == ('YES')):
    wind = input('Is it windy?: ')
    if wind == ('yes'):
        print('It is too windy for an umbrella')
    else:
        print('Take an umbrella')
else:
    print('Enjoy your day')