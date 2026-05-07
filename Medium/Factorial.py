# Given a number n, print its factorial (n! = 1 * 2 * ... * n).
# Input: n = 5
# Output: 120

n = int(input("Enter a number: "))

fact = 1
for i in range(2, n + 1):
    fact *= i

print(fact)
