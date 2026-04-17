# Given two numbers a and b: if a is even, print a then b; otherwise print b then a.
# Input: a = 2, b = 3
# Output: 2 3
# Input: a = 5, b = 8
# Output: 8 5

a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a % 2 == 0:
    print(a, b)
else:
    print(b, a)
