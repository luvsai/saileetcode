# Last updated: 18/12/2025, 20:19:00
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insindex = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[insindex] = nums[i]
                insindex +=1
        while insindex < n:
            nums[insindex] = 0
            insindex +=1
