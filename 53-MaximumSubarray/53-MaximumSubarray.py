# Last updated: 18/12/2025, 20:20:53
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maxsum = nums[0]
        # cursum = nums[0]
        # for i in range(1, len(nums)):
        #     if cursum < 0:
        #         cursum = 0
        #     cursum += nums[i]
        #     maxsum = max(cursum, maxsum)
        # return maxsum
        currsum = 0
        maxsum = float('-inf')
        for i in nums:
            currsum += i
            maxsum = max(currsum, maxsum)
            currsum = (0 if currsum < 0 else currsum)
        return maxsum


        # i = 1

        # pos1=0
        
        # pos2=0
        # maxsum = nums[0]
        # csum = nums[0]
        # while i< len(nums):
        #     if csum < 0:  
        #         pos1 = i 
        #         csum = 0
        #     csum += nums[i]
        #     if csum > maxsum:
        #         pos2 = i
        #         maxsum = csum
        #     i +=1
        # return maxsum
