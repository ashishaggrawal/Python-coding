# Given a string s, print the characters at even positions (2nd, 4th, 6th, ...) in a single line.
# Positions are counted starting from 1.
# Examples:

# Input: s = "Python"
# Output: y h n
# Input: s = "Programming"
# Output: r g a m n

s = input("Enter a string: ")

for i in range(1, len(s), 2):
    print(s[i], end=" ")

print()
