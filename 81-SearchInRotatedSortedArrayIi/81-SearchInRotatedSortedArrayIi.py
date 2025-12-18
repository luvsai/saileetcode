# Last updated: 18/12/2025, 20:20:27
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] and nums[mid] == nums[r]:
                l +=1 
                r -=1
                continue
            # Check if the left side is sorted
            if nums[l] <= nums[mid]:  # Changed to <= to handle duplicates
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:  # Right side must be sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return False
        