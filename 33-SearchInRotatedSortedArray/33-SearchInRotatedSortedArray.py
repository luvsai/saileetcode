# Last updated: 18/12/2025, 20:21:16
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Write your code here
        n = len(nums)
        
        l = 0 ; r = n-1
        k = target
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] == k:
                return mid
            #check if left sorted
            if nums[l] <= nums[mid] :
                if nums[l] <= k < nums[mid]:
                    r = mid - 1
                else :
                    l = mid + 1
            else:# right sorted
                if nums[mid] < k  <= nums[r]:
                    l = mid +1
                else :
                    r = mid -1
        return -1
