# Last updated: 18/12/2025, 20:20:02
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, j):
            # Base cases
            if j < 0:   # t finished
                return 1
            if i < 0:   # s finished first
                return 0
            
            if s[i] == t[j]:
                # take or skip
                return dfs(i - 1, j - 1) + dfs(i - 1, j)
            else:
                # skip s[i]
                return dfs(i - 1, j)
        
        return dfs(len(s) - 1, len(t) - 1)
