'''Convert a few decimal numbers to binary, and a few binary numbers back
to decimal, by working through the place values (128, 64, 32, ... 1).
Python's bin() and int(..., 2) are used to check the answers.'''

# Decimal to binary by hand (place values: 128 64 32 16 8 4 2 1)
# 11  = 8 + 2 + 1            -> 00001011
# 65  = 64 + 1               -> 01000001
# 100 = 64 + 32 + 4          -> 01100100
# 255 = all bits on          -> 11111111

print('Decimal to binary')
print(11, '->', bin(11))
print(65, '->', bin(65))
print(100, '->', bin(100))
print(255, '->', bin(255))

# Binary to decimal by hand
# 1101     = 8 + 4 + 1       -> 13
# 1000     = 8               -> 8
# 101011   = 32 + 8 + 2 + 1  -> 43

print()
print('Binary to decimal')
print('1101   ->', int('1101', 2))
print('1000   ->', int('1000', 2))
print('101011 ->', int('101011', 2))
