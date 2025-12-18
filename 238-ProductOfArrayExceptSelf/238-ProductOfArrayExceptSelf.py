# Last updated: 18/12/2025, 20:19:10
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1]* n
        left = 1
        for i in range(0, n):
            output[i] = left 
            left = output[i] * nums[i]
        right = 1
        for i in range(n-1, -1, -1):
            output[i] *= right 
            right *= nums[i]
        return output