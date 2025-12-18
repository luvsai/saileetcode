# Last updated: 18/12/2025, 20:18:32
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # nums.sort()
        # res = []
        # expected = 1
        # for x in nums:
        #     while expected < x:
        #         res.append(expected)
        #         expected +=1
        #     if x == expected:
        #         expected +=1
        # while expected <= len(nums):
        #     res.append(expected)
        #     expected +=1
        # return res

        # mark seen numbers by making the index negative
        for i in range(len(nums)):
            index = abs(nums[i]) -1
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        res = []
        for i in range(len(nums)):
            if nums[i] > 0 :
                res.append(i + 1)
        return res