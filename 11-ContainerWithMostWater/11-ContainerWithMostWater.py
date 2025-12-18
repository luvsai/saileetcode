# Last updated: 18/12/2025, 20:21:28
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxwater = 0
        n = len(height)
        left = 0
        right = n -1
        while left < right:
            width = right - left
            
            minlen = min(height[left], height[right])
            area = width * minlen
            maxwater = max(area, maxwater)

            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return maxwater
        