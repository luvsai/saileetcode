# Last updated: 18/12/2025, 20:21:25
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for i in range(len(nums) -2):
            left, right = i +1 , len(nums)-1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                #update the closest seen so fat
                if abs(s - target) < abs(closest - target):
                    closest = s
                
                if s < target:
                    left +=1
                elif s > target:
                    right -=1
                else:
                    return s
        return closest