# Given n non-negative integers representing an elevation map where each bar has
# width 1, compute how much water it can trap after raining.
# Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Output: 6
# Input: height = [4, 2, 0, 3, 2, 5]
# Output: 9

# Approach: water above a bar = min(tallest bar on its left, tallest on its right) - its
# height. Two pointers track the max from each side; whichever side has the smaller max
# is the limiting wall, so that side's water can be settled and its pointer moved.
# Time: O(n)  Space: O(1)


def trap(height):
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0
    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]
    return water


if __name__ == "__main__":
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(trap([4, 2, 0, 3, 2, 5]))                    # 9
