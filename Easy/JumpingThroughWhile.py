# Given a number n, use a while loop to print numbers from 1 to n jumping by 2.
# Input: n = 10
# Output: 1 3 5 7 9

n = int(input("Enter a number: "))

i = 1
while i <= n:
    print(i, end=" ")
    i += 2

print()
