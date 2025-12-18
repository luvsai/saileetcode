# Last updated: 18/12/2025, 20:21:08
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # step 1 remove all the invalid numbers
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n+1
        
        #step2 mark presence

        for num in nums:
            num = abs(num)
            if 1 <= num <= n:
                nums[num-1] = -abs(nums[num-1])
        
        #step3 first missing positive
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n+1
