# Last updated: 18/12/2025, 20:19:09
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 ,c1c, c2, c2c = None, 0 , None, 0
        n = len(nums)
        for i in nums:
            if i == c1:
                c1c +=1
            elif i == c2:
                c2c += 1
            elif c1c == 0:
                c1 ,c1c = i , 1
            elif c2c == 0:
                c2, c2c = i, 1
            else:
                c1c -=1
                c2c -=1
        count1 , count2 = 0,0
        for i in nums:
            if i == c1:
                count1 += 1
            elif i == c2:
                count2 += 1
        ar = []
        r = n//3
        if count1 > r:
            ar.append(c1)
        if count2 > r:
            ar.append(c2)
        return ar
        