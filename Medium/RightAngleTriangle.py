# Given a number n, print a right angle triangle of stars with n rows.
# Input: n = 4
# Output:
# *
# * *
# * * *
# * * * *

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
