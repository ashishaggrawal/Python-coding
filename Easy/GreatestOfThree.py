# Given three numbers a, b and c, print the greatest of them.
# Input: a = 10, b = 3, c = 2
# Output: 10

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a >= b and a >= c:
    print(a)
elif b >= c:
    print(b)
else:
    print(c)
