# Last updated: 18/12/2025, 20:17:12
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid) , len(grid[0])
        r,c = 0, n-1
        count = 0

        while r < m and c >= 0:
            if grid[r][c] < 0:
                # All numbers to the left of c are also negative
                count += (m-r)
                c -= 1 # move left
            else:
                r += 1 # move down
        return count