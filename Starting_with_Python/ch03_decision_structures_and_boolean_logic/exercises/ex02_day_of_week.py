'''Ask for a number from 1 to 7 and display the matching day of the
week (1 = Monday ... 7 = Sunday). Any other number shows an error.'''

day_number = int(input('Enter a number (1-7): '))

if day_number == 1:
    day = 'Monday'
elif day_number == 2:
    day = 'Tuesday'
elif day_number == 3:
    day = 'Wednesday'
elif day_number == 4:
    day = 'Thursday'
elif day_number == 5:
    day = 'Friday'
elif day_number == 6:
    day = 'Saturday'
elif day_number == 7:
    day = 'Sunday'
else:
    day = ''

if day:
    print(f'Day {day_number} is {day}.')
else:
    print('Error: the number must be between 1 and 7.')
