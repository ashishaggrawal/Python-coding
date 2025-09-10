# Given a string s, find the length of the longest substring without repeating characters.
# Input: s = "abcabcbb"
# Output: 3   ("abc")
# Input: s = "pwwkew"
# Output: 3   ("wke")

# Approach: slide a window [left, right] and remember the last index of each character.
# When a character repeats inside the window, jump left to just past its previous index
# instead of shrinking one step at a time.
# Time: O(n)  Space: O(min(n, alphabet size))


def length_of_longest_substring(s):
    last_seen = {}  # char -> last index
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # 3
    print(length_of_longest_substring("bbbbb"))     # 1
    print(length_of_longest_substring("pwwkew"))    # 3
    print(length_of_longest_substring(""))          # 0
