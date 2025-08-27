# Given an integer array nums, return all unique triplets [a, b, c] such that
# a + b + c == 0. The result must not contain duplicate triplets.
# Input: nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
# Input: nums = [0, 0, 0]
# Output: [[0, 0, 0]]

# Approach: sort, then fix each number as the first element and use two pointers on the
# rest to find pairs summing to its negative. Skip equal neighbours to avoid duplicates.
# Time: O(n^2)  Space: O(1) extra (ignoring the sort and output)


def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break  # sorted, so no three numbers from here can sum to 0
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
    return result


if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
    print(three_sum([0, 1, 1]))              # []
    print(three_sum([0, 0, 0]))              # [[0, 0, 0]]
