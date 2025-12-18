# Last updated: 18/12/2025, 20:20:51
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        result = []

        top, bottom = 0, len(matrix) -1
        left, right = 0, len(matrix[0]) -1

        while top <= bottom and left <= right:

            # 1 . Traverse top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top+=1

            # 2. travverse the last col
            for row in range(top, bottom +1):
                result.append(matrix[row][right])
            right -=1

            # traverse bottom row (if still valid)
            if top <= bottom :
                for col in range(right, left -1, -1):
                    result.append(matrix[bottom][col])
                bottom -=1
            
            # traverse left column if still valid
            if left <= right:
                for row in range(bottom, top-1 , -1):
                    result.append(matrix[row][left])
                left +=1
        return result
            


        # m = len(matrix) ; n = len(matrix[0])
        # ans = []
        # def dfs(x,y):
        #     nonlocal ans
        #     answer.append()
        #     directions = [(0,1),(1,0),(0-1),(-1,0)]
        #     for dx, dy in directions:
        #         nx = x + dy; ny = y + dy

        #         if 0<= nx < m and 0<=ny<= n:

        #             dfs(index) 
