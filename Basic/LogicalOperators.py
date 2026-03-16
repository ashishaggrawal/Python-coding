# Given two numbers a and b, use the logical operators and, or, not.
# Input: a = 5, b = 0
# Output:
# a > 0 and b > 0: False
# a > 0 or b > 0: True
# not (a > 0): False

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("a > 0 and b > 0:", a > 0 and b > 0)
print("a > 0 or b > 0:", a > 0 or b > 0)
print("not (a > 0):", not (a > 0))
