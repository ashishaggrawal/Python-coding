# Given a number n, print all numbers from n down to 1 in a single line, separated by spaces.
# Input: n = 5
# Output: 5 4 3 2 1

n = int(input("Enter a number: "))

for i in range(n, 0, -1):
    print(i, end=" ")

print()
