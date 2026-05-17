# Given a number n, print the nth Fibonacci number (1, 1, 2, 3, 5, 8, ...).
# Input: n = 6
# Output: 8

n = int(input("Enter a number: "))

a, b = 0, 1
for i in range(n):
    a, b = b, a + b

print(a)
