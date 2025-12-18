# Last updated: 18/12/2025, 20:19:18
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[-1]
        n_1 = n-1

        dp1 = [0] * n_1
        dp2 = [0] * n_1
        dp1[0] = nums[0]
        dp2[0] = nums[1]
        for i in range(1,n_1):
            #dp1
                #vis
            vp = nums[i]
            if i > 1:
                vp += dp1[i-2]
            nvp = dp1[i-1]
            dp1[i] = max(vp,nvp) 

            #dp2
            vp = nums[i + 1]
            if i > 1:
                vp += dp2[i-2]
            nvp = dp2[i-1]
            dp2[i] = max(vp,nvp) 
        return max(dp1[-1],dp2[-1])
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob_linear(houses):
            n = len(houses)
            dp = [0] * n
            dp[0] = houses[0]
            if n > 1:
                dp[1] = max(houses[0], houses[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + houses[i])
            return dp[-1]
        
        # Scenario 1: Exclude the first house
        max_exclude_first = rob_linear(nums[1:])
        
        # Scenario 2: Exclude the last house
        max_exclude_last = rob_linear(nums[:-1])
        
        # Return the maximum of both scenarios
        return max(max_exclude_first, max_exclude_last)