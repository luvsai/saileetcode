# Last updated: 18/12/2025, 20:19:33
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0; right = n -1
        left , right = 0, len(nums)-1

        while left < right:
            mid = left + (right - left) //2 # this makes sure mid+1 is alway <= high
            if nums[mid] < nums[mid+1] :
                left = mid +1
            else :
                right = mid
        return left 

        # while left < right:
        #     # mid = (left + right) // 2
        #     mid = left + (right -left) //2
        #     mid_left = nums[mid-1] if mid>0 else float('-inf')
        #     mid_right = nums[mid+1] if mid< n-1 else float('-inf')

        #     if nums[mid] > mid_left and nums[mid] > mid_right:
        #         return mid
        #     elif mid_right > nums[mid]:
        #         left = mid +1
        #     else :
        #         right = mid -1
        

        return left
        