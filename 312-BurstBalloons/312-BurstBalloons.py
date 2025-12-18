# Last updated: 18/12/2025, 20:18:51
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # bottom up tabulation
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        #lenght of interval
        for length in range(1, n-1):
            for i in range(1, n-length):
                j = i + length -1
                for k in range(i, j+1):
                    dp[i][j] = max(dp[i][j], dp[i][k-1] + dp [k +1][j] + nums[i-1] * nums[k] * nums[j + 1])
        return dp[1][n-2]




        # memoization top down
        nums = [1] + nums + [1]
        n = len(nums)
        dp = {}

        def solve(i,j) :
            if i > j:
                return 0
            if (i, j) in dp :
                return dp[(i,j)]
            ans = 0
            for k in range(i, j +1):
                coins = solve(i,k -1) + solve(k + 1, j)
                coins += nums[i-1] * nums[k] * nums [j +1] 
                ans = max(ans, coins)
            dp[(i,j)] = ans
            return ans

        if 1 ==1:
            return solve(1, n-2)
        # below is version with out padding 1 on both sides
        n = len(nums)
        def f(i,j):
            if (i < 0 or j > n-1) and i>j:
                return 0
            if i == j:
                left, right = 1,1
                
                if i > 0 :
                    left = nums[i-1]
                if j < (n-1):
                    right = nums[j+1]
                return left * nums[i] * right
            maxcoins = 0
            for k in range(i, j+1):
                coins = f(i, k -1) + f(k +1 , j)
                left, right = 1,1
                
                if i > 0 :
                    left = nums[i-1]
                if j < (n-1):
                    right = nums[j+1]
                coins +=  left * nums[k]* right 
                maxcoins = max(maxcoins, coins)
            return maxcoins
        return f(0, n-1)
                    


        