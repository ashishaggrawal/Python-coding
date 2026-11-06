'''One acre of land is 43,560 square feet. Ask the user for the size of a
piece of land in square feet and show how many acres it is.'''

SQ_FEET_PER_ACRE = 43560

square_feet = float(input('Enter the land size in square feet: '))

acres = square_feet / SQ_FEET_PER_ACRE

print(f'That is {acres:,.2f} acres.')
