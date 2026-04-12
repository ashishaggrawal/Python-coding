# Given a number n, print whether it is Positive, Negative or Zero using if / elif / else.
# Input: n = 7
# Output: Positive
# Input: n = -3
# Output: Negative

n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
