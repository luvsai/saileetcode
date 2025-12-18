# Last updated: 18/12/2025, 20:18:39
class Solution:
#     . Real-world intuition (SUPER IMPORTANT)
# Imagine you have:
# A long road
# With checkpoints (array values)
# And you need to split the road into m segments
# You want the maximum distance among these segments to be as small as possible
# This is EXACTLY what the problem is doing

# Let:
# lo = max(nums) → the minimum possible maximum sum
# (because one segment must at least contain the largest element)
# hi = sum(nums) → max possible maximum sum (no splits)

# We want the minimum X such that:
# Can we split the array into at most m subarrays
# such that each subarray has sum ≤ X?
# This forms:
# \U0001f4a1 Binary Search on the answer X
    def splitArray(self, nums: List[int], k: int) -> int:
        def cansplit(nums, k, max_sum):
            current = 0
            parts = 1
            for num in nums:
                if current + num > max_sum:
                    parts +=1
                    current = num
                    if parts > k:
                        return False
                else:
                    current += num
            return True
        low = max(nums)
        high = sum(nums)

        while low< high:
            mid = (low + high) //2
            if cansplit(nums, k , mid):
                high = mid
            else:
                low = mid + 1
        return low