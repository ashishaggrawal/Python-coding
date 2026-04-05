# Given a number n, use a while loop to print its multiplication table in reverse (10*n down to n).
# Input: n = 2
# Output: 20 18 16 14 12 10 8 6 4 2

n = int(input("Enter a number: "))

i = 10
while i >= 1:
    print(n * i, end=" ")
    i -= 1

print()
