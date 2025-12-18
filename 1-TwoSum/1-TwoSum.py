# Last updated: 18/12/2025, 20:21:36
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         setB = dict()
#         j = 0
#         for i in nums:
#             if setB.get(target-i) != None :
#                 return [setB[target-i], j]
#             setB[i] = j
#             j += 1

class Solution:
    def twoSum (self, nums: List[int] , target: int) -> List[int]:
        # setB = dict()
        # j = 0
        # for i in nums:
        #     if setB.get(target - i ) != None:
        #         return [setB[target -i], j]
        #     setB[i] = j
        #     j += 1

        hashmap = {}
        j = 0
        for el in nums:
            complement = target - el
            if complement in hashmap:
                return [hashmap[complement], j]
            else:
                hashmap[el] = j
            j+=1
        
