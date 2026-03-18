# Given two numbers a and b, print the result of every bitwise operator.
# Input: a = 6 (110), b = 3 (011)
# Output:
# a & b: 2
# a | b: 7
# a ^ b: 5
# ~a: -7
# a << 1: 12
# a >> 1: 3

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("a & b:", a & b)      # AND: 1 only where both bits are 1
print("a | b:", a | b)      # OR: 1 where either bit is 1
print("a ^ b:", a ^ b)      # XOR: 1 where the bits are different
print("~a:", ~a)            # NOT: flips all bits, equals -(a + 1)
print("a << 1:", a << 1)    # left shift: multiplies by 2
print("a >> 1:", a >> 1)    # right shift: divides by 2 (floor)
