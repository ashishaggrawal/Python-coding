# Given two numbers a and b, print their GCD (Greatest Common Divisor).
# Input: a = 12, b = 18
# Output: 6

a = int(input("Enter a: "))
b = int(input("Enter b: "))

while b != 0:
    a, b = b, a % b

print(a)
