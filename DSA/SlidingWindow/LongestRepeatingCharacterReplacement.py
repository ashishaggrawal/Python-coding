# Given a string s of uppercase letters and an integer k, you may change at most k
# characters to any other uppercase letter. Return the length of the longest substring
# that can be made of a single repeated letter.
# Input: s = "ABAB", k = 2
# Output: 4
# Input: s = "AABABBA", k = 1
# Output: 4

# Approach: a window is valid if (window length - count of its most frequent letter) <= k,
# since that many letters need replacing. Grow the window to the right and shift left by
# one whenever it becomes invalid. max_freq never needs to decrease: only a higher max_freq
# can produce a longer answer.
# Time: O(n)  Space: O(26)

from collections import defaultdict


def character_replacement(s, k):
    count = defaultdict(int)
    left = 0
    max_freq = 0
    best = 0
    for right, ch in enumerate(s):
        count[ch] += 1
        max_freq = max(max_freq, count[ch])
        if (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    print(character_replacement("ABAB", 2))     # 4
    print(character_replacement("AABABBA", 1))  # 4
