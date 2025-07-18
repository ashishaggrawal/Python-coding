# Given an array of strings, group the anagrams together. An anagram uses exactly the
# same letters as another word, in a different order.
# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

# Approach: anagrams share the same letter counts, so a tuple of 26 counts works as a
# dictionary key. This avoids sorting each word (O(k log k)) and costs O(k) per word.
# Time: O(n * k)  Space: O(n * k)   (n words, k = longest word length)

from collections import defaultdict


def group_anagrams(strs):
    groups = defaultdict(list)
    for word in strs:
        count = [0] * 26
        for ch in word:
            count[ord(ch) - ord("a")] += 1
        groups[tuple(count)].append(word)
    return list(groups.values())


if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    print(group_anagrams([""]))   # [['']]
    print(group_anagrams(["a"]))  # [['a']]
