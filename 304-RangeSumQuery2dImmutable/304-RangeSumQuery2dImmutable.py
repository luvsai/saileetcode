# Last updated: 18/12/2025, 20:18:54
from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.prefixsum = [] 
            return

        self .prefixsum = [row[:] for row in matrix]
        
        for i in range(0, len(matrix)):
            for j in range(1, len(matrix[0])):
                self.prefixsum[i][j] += self.prefixsum[i][j-1]
        for j in range(0, len(matrix[0])):
            for i in range(1, len(matrix)):
                self.prefixsum[i][j] += self.prefixsum[i-1][j]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.prefixsum[row2][col2]
        
        if row1 >= 1:
            ans -= self.prefixsum[row1 -1][col2]
        if col1 >= 1:
            ans -= self.prefixsum[row2][col1 -1]
        if row1 >=1 and col1 >=1:
            ans += self.prefixsum[row1-1][col1-1] 
        
        return ans