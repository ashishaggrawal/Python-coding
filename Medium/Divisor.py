# Given a number n, print all of its divisors in increasing order.
# Input: n = 12
# Output: 1 2 3 4 6 12

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")

print()
