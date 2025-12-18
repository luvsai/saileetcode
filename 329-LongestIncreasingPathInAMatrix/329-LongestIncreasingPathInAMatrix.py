# Last updated: 18/12/2025, 20:18:47
from functools import lru_cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # Step 1: Compute indegree for each cell
        indegree = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                        indegree[x][y] += 1
        
        # Step 2: Multisource BFS starting from all indegree 0 nodes
        q = deque()
        for i in range(m):
            for j in range(n):
                if indegree[i][j] == 0:
                    q.append((i, j))
        
        # Step 3: BFS layers = path length
        longest_path = 0
        
        while q:
            longest_path += 1  # every layer increases path length by 1
            
            for _ in range(len(q)):
                i, j = q.popleft()
                
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                        indegree[x][y] -= 1
                        
                        if indegree[x][y] == 0:
                            q.append((x, y))
        
        return longest_path
        m , n = len(matrix) , len(matrix[0])
        directions = [(0,1) ,(1,0), (-1,0) , (0,-1)]
        dp = {}
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            longest = 1
            
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0<= y< n and matrix[x][y] > matrix[i][j] :
                    longest = max(longest , 1 + dfs(x, y))
            dp[(i,j)] = longest
            return longest
        ans = 0

        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans
        # lets try iterative approach


