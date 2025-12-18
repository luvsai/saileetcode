# Last updated: 18/12/2025, 20:20:45
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]* n for _ in range(n)]

        top, bottom = 0, n -1
        left, right = 0, n -1
        counter = 1
        while top <= bottom and left <= right:

            # 1 . Traverse top row
            for col in range(left, right + 1):
                matrix[top][col] = counter
                counter +=1
            top+=1
            

            # 2. travverse the last col
            for row in range(top, bottom +1):
                matrix[row][right]  = counter
                counter +=1
            right -=1
            

            # traverse bottom row (if still valid)
            if top <= bottom :
                for col in range(right, left -1, -1):
                    matrix[bottom][col]  = counter
                    counter +=1
                bottom -=1
                
            
            # traverse left column if still valid
            if left <= right:
                for row in range(bottom, top-1 , -1):
                    matrix[row][left]  = counter
                    counter +=1
                left +=1
        return matrix