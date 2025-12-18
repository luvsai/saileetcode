# Last updated: 18/12/2025, 20:18:27
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hmap  = {}

        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]  :
                idx = stack.pop()
                hmap[nums2[idx]] = nums2[i]
            stack.append(i)	
        return [hmap.get(i,-1) for i in nums1]