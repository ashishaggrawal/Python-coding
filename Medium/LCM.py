# Given two numbers a and b, print their LCM (Least Common Multiple).
# LCM(a, b) = a * b / GCD(a, b)
# Input: a = 4, b = 6
# Output: 12

a = int(input("Enter a: "))
b = int(input("Enter b: "))

x, y = a, b
while y != 0:
    x, y = y, x % y

print(a * b // x)
