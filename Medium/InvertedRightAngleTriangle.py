# Given a number n, print an inverted right angle triangle of stars with n rows.
# Input: n = 4
# Output:
# * * * *
# * * *
# * *
# *

n = int(input("Enter a number: "))

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
