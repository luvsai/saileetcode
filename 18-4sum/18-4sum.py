# Last updated: 18/12/2025, 20:21:24
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort the array to make it easier to skip duplicates
        n = len(nums)
        quads = []

        for i in range(n - 3):  # First pointer
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements

            for j in range(i + 1, n - 2):  # Second pointer
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue  # Skip duplicate elements

                left, right = j + 1, n - 1  # Two pointers for the remaining part of the array

                while left < right:
                    sum_4 = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if sum_4 == target:
                        quads.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1  # Skip duplicate elements
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1  # Skip duplicate elements
                        
                        left += 1
                        right -= 1
                    
                    elif sum_4 < target:
                        left += 1  # Increase sum by moving the left pointer right
                    else:
                        right -= 1  # Decrease sum by moving the right pointer left

        return quads
