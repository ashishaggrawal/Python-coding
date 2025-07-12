# Given an integer array nums, return True if any value appears at least twice,
# and False if every element is distinct.
# Input: nums = [1, 2, 3, 1]
# Output: True
# Input: nums = [1, 2, 3, 4]
# Output: False

# Approach: add each number to a hash set and stop as soon as one is already there.
# Time: O(n)  Space: O(n)


def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))                    # True
    print(contains_duplicate([1, 2, 3, 4]))                    # False
    print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
