# Given two numbers a and b, swap them and print the new values.
# Input: a = 10, b = 20
# Output: 20 10

a = int(input("Enter a: "))
b = int(input("Enter b: "))

a, b = b, a

print(a, b)
