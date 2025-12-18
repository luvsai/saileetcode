# Last updated: 18/12/2025, 20:19:32
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = -1
        count = 0
        for element in nums :
            if count == 0:
                candidate = element
            if candidate == element:
                count +=1
            else:
                count -=1
        return candidate
