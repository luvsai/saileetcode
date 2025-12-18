# Last updated: 18/12/2025, 20:19:28
class Solution:

# dp[i] implies maximum amt of money you can rob # #visiting home at index and leave without alarming police.

#dp[i] = max(amt[i] + dp[i-2] , dp[i-1])



    nums = []
    def vis(self,i):
        if i == 0:
            return self.nums[0]
        #visiting 
        vp = self.nums[i] 
        if i > 1:
            vp +=  self.vis(i - 2)
        #notvisiting
        nvp = self.vis(i-1)

        return max(vp,nvp)



    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        phouse , pphouse  = max(nums[0], nums[1]), nums[0]
        for i in range(2, n):
            pphouse ,phouse = phouse, max(nums[i] + pphouse , phouse)
        return phouse 

        # n = len(nums)
        # maxp = 0
        # if n == 1:
        #     return nums[0]
        # if n == 2:
        #     maxp = max(nums)
        #     return maxp
        # phouse = maxp
        # pphouse = nums[0]

        
        # for i in range(2,n):
        #     maxp = max(nums[i] + pphouse, phouse)
        #     pphouse = phouse
        #     phouse = maxp
        # return maxp

        
        # n = len(nums)
        # self.nums = nums
        # return self.vis(n-1)
        # #recurssion
        

        # dp = [-1] * n
        # dp[0] = nums[0]
        # for i in range(1, n):
        #     maxp = nums[i] 
        #     if i > 1:
        #         maxp += dp[i-2]
        #     maxnp = dp[i-1]
        #     dp[i] = max(maxp,maxnp)
        # return dp[-1]
        