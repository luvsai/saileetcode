# Last updated: 18/12/2025, 20:20:59
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n= len(matrix[0])
        for i in range(0,m):
            for j in range(0,n):
                if i > j:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
        for i in range(m):
            for j in range(n//2):
                temp = matrix[i][j]
                matrix[i][j]= matrix[i][n-1-j]
                matrix[i][n -1 -j] = temp
        return matrix
