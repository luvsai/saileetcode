# Last updated: 18/12/2025, 20:17:00
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        farr = [[0 for _ in range(n)] for p in range(m)]
        for i in range(m):
            for j in range(n):
                update = min(rowSum[i], colSum[j])
                farr[i][j] = update
                rowSum[i] -= update
                colSum[j] -=update
        return farr 
        