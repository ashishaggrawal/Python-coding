# Given an array height of n vertical lines, find two lines that together with the
# x-axis form a container holding the most water. Return that maximum amount.
# Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49   (lines at index 1 and 8: min(8, 7) * 7)
# Input: height = [1, 1]
# Output: 1

# Approach: start with the widest container and move the shorter line inward. Moving
# the taller line can never help, because the width shrinks and the height is still
# limited by the shorter line.
# Time: O(n)  Space: O(1)


def max_area(height):
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        best = max(best, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best


if __name__ == "__main__":
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(max_area([1, 1]))                       # 1
