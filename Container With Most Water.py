11. Container With Most Water
Medium

class Solution(object):
    def maxArea(self, height):
        maxArea = 0
        left = 0
        right = len(height) - 1
        while left < right:
            shorter_distance = min(height[left], height[right])
            maxArea = max(maxArea, shorter_distance * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
