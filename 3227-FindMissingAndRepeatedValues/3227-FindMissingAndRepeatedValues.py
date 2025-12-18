# Last updated: 18/12/2025, 20:16:42
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        b = set()
        m , n = len(grid), len(grid[0])
        duplicate = -1
        missing = -1
        for i in range (m):
            for j in range(n):
                el = grid[i][j]
                if el in b:
                    duplicate = el
                else:
                    b.add(el)
        for i in range(1, m*n + 1):
            if i not in b:
                missing = i
        return [duplicate, missing]

                