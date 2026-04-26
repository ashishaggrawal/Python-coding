# Given two numbers n and m, print the difference of their multiplication tables
# (n*i - m*i for i from 1 to 10) in a single line.
# Input: n = 5, m = 3
# Output: 2 4 6 8 10 12 14 16 18 20

n = int(input("Enter n: "))
m = int(input("Enter m: "))

for i in range(1, 11):
    print(n * i - m * i, end=" ")

print()
