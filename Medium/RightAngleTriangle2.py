# Given a number n, print a right angle triangle of numbers with n rows.
# Input: n = 4
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
