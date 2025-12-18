# Last updated: 18/12/2025, 20:18:25
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ans = [-1] * n
        
        for i in range(2 *n):
            num = nums[i% n]
            while stack and nums[stack[-1]] < num:
                idx = stack.pop()
                ans[idx] = num
            if i < n:
                stack.append(i)
        return ans