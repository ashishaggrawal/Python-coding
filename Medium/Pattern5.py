# Given a number n, print the following inverted number pattern.
# Input: n = 4
# Output:
# 1 2 3 4
# 1 2 3
# 1 2
# 1

n = int(input("Enter a number: "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
