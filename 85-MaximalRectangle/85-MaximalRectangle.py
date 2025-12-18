# Last updated: 18/12/2025, 20:20:24
class Solution:
    def largestRectangleArea(self, heights):
        area = 0
        stack = [-1]
        heights.append(0)
        for i , h in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] > h:
                idx = stack.pop()
                height = heights[idx]
                width =  i - stack[-1] -1 #expands until the stack top the same height
                area = max(area, height * width)
            stack.append(i)

        return area




    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n = len(matrix[0])
        heights = [0] * n
        max_area = 0
        
        for row in matrix:
            for i , val in enumerate(row):
                if val == '1':
                    heights[i] +=1
                else:
                    heights [i] = 0 # since as we accumulate rows if there is nto base pillar the building cannot stay on above.
            
            # compute the largest reactangle in histogram for this row
            max_area = max(max_area, self.largestRectangleArea(heights))
        return max_area
