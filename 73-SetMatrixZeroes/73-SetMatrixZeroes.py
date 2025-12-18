# Last updated: 18/12/2025, 20:20:35
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])

        frz = any(matrix[0][c] == 0 for c in range(cols))
        fcz = any(matrix[r][0] == 0 for r in range(rows))

        # step 2 mark rows and columns 

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        # step 3 zero based on marker
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        # step 4 zero first ro wif needed
        if frz :
            for c in range(cols):
                matrix[0][c] = 0
        # step 5 zero first col if needed
        if fcz :
            for r in range(rows):
                matrix[r][0]= 0
        

        



        