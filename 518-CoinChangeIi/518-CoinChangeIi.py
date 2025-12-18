# Last updated: 18/12/2025, 20:18:22
from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)

        # ----------------------------------------------------
        # dp[i][j] = number of ways to form sum j 
        #            using first i coins
        # ----------------------------------------------------
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # ----------------------------------------------------
        # Base Case: amount 0 can always be formed in 1 way
        # ----------------------------------------------------
        for i in range(n + 1):
            dp[i][0] = 1

        # ----------------------------------------------------
        # Build DP table
        # ----------------------------------------------------
        for i in range(1, n + 1):
            coin = coins[i - 1]

            for j in range(0, amount + 1):

                # Option 1: don't use this coin
                dp[i][j] = dp[i - 1][j]

                # Option 2: use this coin (if possible)
                if j >= coin:
                    dp[i][j] += dp[i][j - coin]

        # ----------------------------------------------------
        # Final answer
        # ----------------------------------------------------
        return dp[n][amount]