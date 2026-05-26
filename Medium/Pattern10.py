# Given a number n, print the following star pattern (grows to n, then shrinks back).
# Input: n = 3
# Output:
# *
# * *
# * * *
# * *
# *

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print("* " * i)

for i in range(n - 1, 0, -1):
    print("* " * i)
