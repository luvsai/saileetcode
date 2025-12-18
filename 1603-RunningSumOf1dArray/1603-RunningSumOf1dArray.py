# Last updated: 18/12/2025, 20:17:05
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rsum = 0
        res = []
        for num in nums:
            rsum += num
            res.append(rsum)
        return res