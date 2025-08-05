# Given a string s, return True if it is a palindrome after converting all uppercase
# letters to lowercase and removing all non-alphanumeric characters.
# Input: s = "A man, a plan, a canal: Panama"
# Output: True
# Input: s = "race a car"
# Output: False

# Approach: two pointers move inward from both ends, skipping characters that are not
# letters or digits, and compare the rest case-insensitively. No cleaned copy is built.
# Time: O(n)  Space: O(1)


def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("race a car"))                      # False
    print(is_palindrome(" "))                               # True
