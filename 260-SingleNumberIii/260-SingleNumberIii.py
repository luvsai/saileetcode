# Last updated: 18/12/2025, 20:19:04
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        for n in nums:
            xor_all = xor_all ^ n

        # get the right most bit which is different in the both numbers
        diffbit = xor_all & -xor_all
        x = 0
        y = 0
        for n in nums:
            if n & diffbit:
                x = x ^ n
            else:
                y = y ^ n
        return [x,y]

