# Last updated: 18/12/2025, 20:19:01
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        alen = len(nums)
        xorall = 0
        for i in range(alen+1):
            xorall ^= i
        for num in nums:
            xorall ^= num
        return xorall