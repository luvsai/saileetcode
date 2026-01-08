# Last updated: 08/01/2026, 19:54:44
from collections import defaultdict
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numcount = defaultdict(int)
        prefixcount = defaultdict(int)
        for num in nums:
            numcount[num] +=1
        keys =sorted(numcount.keys()) #sort o(nlogn)
        # prefixarr = [0]* len(keys)
        rsum = 0
        for idx,key in enumerate(keys):
            prefixcount[key] = rsum
            rsum += numcount[key]
        newarr = [0]* len(nums)
        for idx , num in enumerate(nums):
            newarr[idx] = prefixcount[nums[idx]]
        return newarr


            



        