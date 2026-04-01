# Given a number n, print all numbers from 1 to n in a single line, separated by spaces.
# Input: n = 5
# Output: 1 2 3 4 5

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i, end=" ")

print()
