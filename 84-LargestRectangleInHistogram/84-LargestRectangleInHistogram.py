# Last updated: 18/12/2025, 20:20:26
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        # sentinal index which will be used stack is empty to push in the first elemnt
        stack = [-1]
        max_area = 0
        for i , h in enumerate(heights):

            #maintain the increasing stack
            while stack[-1] != -1 and heights[stack[-1]] > h:
                idx = stack.pop()
                height = heights[idx]
                width = i - stack[-1] -1
                max_area = max(max_area, height * width)

            # we push the current index
            stack.append(i)
        return max_area
        