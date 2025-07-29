# Given an integer array nums, return an array answer where answer[i] is the product of
# every element except nums[i], without using division.
# Input: nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]
# Input: nums = [-1, 1, 0, -3, 3]
# Output: [0, 0, 9, 0, 0]

# Approach: answer[i] = (product of everything to the left) * (product of everything to
# the right). Fill the prefix products first, then sweep from the right multiplying in a
# running suffix product, reusing the output array.
# Time: O(n)  Space: O(1) extra (the output array does not count)


def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


if __name__ == "__main__":
    print(product_except_self([1, 2, 3, 4]))       # [24, 12, 8, 6]
    print(product_except_self([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
