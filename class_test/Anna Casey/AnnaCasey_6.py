choice = input('Enter a choice of Weather, Day, or Date: ')
if choice == ('Weather'):
    Weather = input('What is the weather like? (sunny or rainy): ')
    if Weather == ('Sunny') or Weather == ('sunny') or Weather == ('SUNNY'):
            print('it is a happy day')
    else:
        print('it is a sad day')
elif choice == ('Date'):
    Date = input('What is the date?: ')
    Date = float(Date)
    if Date %2 == 0:
        print('it is a happy day')
    else:
        print('it is a sad day')
elif choice == ('Day'):
    Day = input('What day of the week is it?: ')
    if Day == ('Sunday') or Day == ('SUNDAY') or Day == ('sunday') or Day == ('Saturday') or Day == ('SATURDAY') or Day == ('saturday'):
        print('It is a happy day')
    else:
        print('it is a sad day')