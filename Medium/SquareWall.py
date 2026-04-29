# Given a number n, print a square wall of n x n stars using nested loops.
# Input: n = 3
# Output:
# * * *
# * * *
# * * *

n = int(input("Enter a number: "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
