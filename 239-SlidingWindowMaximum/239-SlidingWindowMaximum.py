# Last updated: 18/12/2025, 20:19:05
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0; right = 0
        n = len(nums)
        q = deque()
        ans = []
        while right < n:
            val = nums[right]
            while q and q[-1] < val:
                #todo pop all the elments less than val
                q.pop()
            q.append(val)
            if right - left + 1 == k:
                ans.append(q[0])
                # we shrink one step:
                if nums[left] == q[0]:
                    q.popleft()
                left +=1
            right +=1
        return ans
            