'''Ask for the length and width of two rectangles, then say which one
has the bigger area, or whether the areas are the same.'''

length1 = float(input('Length of rectangle 1: '))
width1 = float(input('Width of rectangle 1: '))
length2 = float(input('Length of rectangle 2: '))
width2 = float(input('Width of rectangle 2: '))

area1 = length1 * width1
area2 = length2 * width2

print()
print(f'Area of rectangle 1: {area1:,.2f}')
print(f'Area of rectangle 2: {area2:,.2f}')

if area1 > area2:
    print('Rectangle 1 has the greater area.')
elif area2 > area1:
    print('Rectangle 2 has the greater area.')
else:
    print('Both rectangles have the same area.')
