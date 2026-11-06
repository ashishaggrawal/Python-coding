'''Show the ASCII code of each letter in my first name, to see how
characters are really stored as numbers in memory.'''

# ord() gives the number code for a character
print('A', ord('A'))
print('s', ord('s'))
print('h', ord('h'))
print('i', ord('i'))
print('s', ord('s'))
print('h', ord('h'))

# chr() goes the other way: number code -> character
print(chr(65), chr(115), chr(104), chr(105), chr(115), chr(104))
