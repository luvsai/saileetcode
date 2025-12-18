# Last updated: 18/12/2025, 20:17:08
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxD = deque()
        minD = deque()
        left  = 0
        right = 0

        best = 0
        for right, val in enumerate(nums):
            # maintain maxdeque
            while maxD and maxD[-1] < val:
                maxD.pop()
            maxD.append(val)
            while minD and minD[-1] > val:
                minD.pop()
            minD.append(val)

            while maxD[0] - minD[0] > limit:
                if maxD[0] == nums[left]:
                    maxD.popleft()
                if minD[0] == nums[left]:
                    minD.popleft()
                left +=1

            best = max(best, right -left + 1)

        return best
