# Given an integer n and a string s, print them together on one line.
# An int cannot be added to a str directly, so convert it with str() first.
# Input: n = 5, s = "Apples"
# Output: 5 Apples

n = int(input("Enter a number: "))
s = input("Enter a string: ")

print(str(n) + " " + s)
