'''Ask for a number from 1 to 10 and display it as a Roman numeral.
Numbers outside that range show an error.'''

number = int(input('Enter a number (1-10): '))

if number < 1 or number > 10:
    print('Error: the number must be between 1 and 10.')
else:
    if number == 1:
        numeral = 'I'
    elif number == 2:
        numeral = 'II'
    elif number == 3:
        numeral = 'III'
    elif number == 4:
        numeral = 'IV'
    elif number == 5:
        numeral = 'V'
    elif number == 6:
        numeral = 'VI'
    elif number == 7:
        numeral = 'VII'
    elif number == 8:
        numeral = 'VIII'
    elif number == 9:
        numeral = 'IX'
    else:
        numeral = 'X'

    print(f'{number} in Roman numerals is {numeral}.')
