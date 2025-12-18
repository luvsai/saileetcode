# Last updated: 18/12/2025, 20:17:03
from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat) , len(mat[0])
        rowCount = [0] * rows
        colCount = [0] * cols

        # Count one in each row and column
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] ==1:
                    rowCount[i] += 1
                    colCount[j] += 1
        # Count special positions
        special = 0

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1 and rowCount[i] == 1 and colCount[j] ==1 :
                    special +=1
        return special