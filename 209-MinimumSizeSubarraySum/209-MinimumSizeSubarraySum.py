# Last updated: 18/12/2025, 20:19:21
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]

            #shrink the window while the condition is vaid
            while window_sum >= target :

                #take the length 
                min_len = min(min_len, right -left + 1)

                window_sum -= nums[left]

                left += 1
        return 0 if min_len == float('inf') else min_len