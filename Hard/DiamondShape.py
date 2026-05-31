# Given a number n, print a diamond of stars with 2n - 1 rows.
# Input: n = 3
# Output:
#     *
#   * * *
# * * * * *
#   * * *
#     *

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print("  " * (n - i) + "* " * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print("  " * (n - i) + "* " * (2 * i - 1))
