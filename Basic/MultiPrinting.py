# Given a string s and a number n, print s n times, each on a new line.
# Input: s = Hi, n = 3
# Output:
# Hi
# Hi
# Hi

s = input("Enter a string: ")
n = int(input("Enter a number: "))

for i in range(n):
    print(s)
