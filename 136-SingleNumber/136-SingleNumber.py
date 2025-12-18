# Last updated: 18/12/2025, 20:19:46
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = 0
        for n in nums:
            unique = unique ^ n
        return unique