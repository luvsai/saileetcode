# Last updated: 18/12/2025, 20:19:15
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for el in nums :
            if el in hashset:
                return True
            else:
                hashset.add(el)
        return False