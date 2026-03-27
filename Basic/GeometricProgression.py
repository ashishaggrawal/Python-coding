# Given the first term a, common ratio r and a count n, print the first n terms of the
# geometric progression a, a*r, a*r^2, ...
# Input: a = 2, r = 3, n = 5
# Output: 2 6 18 54 162

a = int(input("Enter first term: "))
r = int(input("Enter common ratio: "))
n = int(input("Enter number of terms: "))

term = a
for i in range(n):
    print(term, end=" ")
    term *= r

print()
