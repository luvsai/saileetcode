# Last updated: 18/12/2025, 20:18:38
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        n = len(nums)

        # ---------------------------------------------
        # dp[i][j] = using first i numbers, can we form sum j?
        # ---------------------------------------------
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        # Base case: sum 0 is always possible (choose nothing)
        for i in range(n + 1):
            dp[i][0] = True

        # ---------------------------------------------
        # Fill DP table
        # ---------------------------------------------
        for i in range(1, n + 1):
            val = nums[i - 1]   # current number

            for j in range(1, target + 1):

                # Option 1: don't take current number
                dp[i][j] = dp[i - 1][j]

                # Option 2: take the number (if possible)
                if j >= val:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - val]

        # ---------------------------------------------
        # Final answer
        # ---------------------------------------------
        return dp[n][target]


# #dp[i][s] =  is it possible to acheive sum s using first i numbers
# # dp[i][s] = dp[i-1][s] or dp[i-1][s- nums[i-1]] # the ith element is included  sum reduces by nums[i-1]
# # return d[n][target]
#         total_sum = sum(nums)
#         if total_sum % 2 != 0:
#             return False
#         target = total_sum //2
#         n = len(nums)
#         dp = [[False ] * (target + 1) for _ in range(n+1)]

#         #base condition : sum 0 is always positive
#         for i in range(n+1):
#             dp[i][0] = True
        
#         for i in range(1,n+1):
#             for s in range(1, target + 1):
#                 if nums[i-1] <= s:
#                     dp[i][s] = dp[i-1] [s] or dp[i-1]
