# Given strings s and t, return the shortest substring of s that contains every character
# of t (including duplicates). Return "" if there is no such substring.
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Input: s = "a", t = "aa"
# Output: ""

# Approach: keep one map of the counts t needs and one of the counts in the window.
# `formed` tracks how many distinct characters currently meet their required count.
# Expand right until the window is valid, then shrink from the left while it stays valid,
# recording the smallest window seen.
# Time: O(len(s) + len(t))  Space: O(len(s) + len(t))

from collections import Counter, defaultdict


def min_window(s, t):
    if not s or not t:
        return ""

    need = Counter(t)
    window = defaultdict(int)
    required = len(need)
    formed = 0
    best_len, best_start = float("inf"), 0

    left = 0
    for right, ch in enumerate(s):
        window[ch] += 1
        if ch in need and window[ch] == need[ch]:
            formed += 1

        while formed == required:
            if right - left + 1 < best_len:
                best_len, best_start = right - left + 1, left
            out = s[left]
            window[out] -= 1
            if out in need and window[out] < need[out]:
                formed -= 1
            left += 1

    return "" if best_len == float("inf") else s[best_start:best_start + best_len]


if __name__ == "__main__":
    print(min_window("ADOBECODEBANC", "ABC"))  # BANC
    print(min_window("a", "a"))                # a
    print(repr(min_window("a", "aa")))         # ''
