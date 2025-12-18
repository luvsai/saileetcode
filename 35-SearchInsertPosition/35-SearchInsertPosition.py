# Last updated: 18/12/2025, 20:21:14
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        n = len(nums)
        right = n-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        return left