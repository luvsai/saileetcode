# Last updated: 18/12/2025, 20:20:30
# class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     ssets = []
    #     n = len(nums)
    #     for i in range(1 << n):
    #         ss = []
    #         for j in range(n):
    #             if i & (1<< j):
    #                 ss.append(nums[j])
    #         ssets.append(ss)
    #     return ssets

class Solution :
	def __init__(self):
		self.auxarr = []
		self.result = []
		self.n = 0
		self.nums = []
	def backtrack(self, startindex ):
		self.result.append(list(self.auxarr))
		
		for i in range(startindex, self.n):
			self.auxarr.append(self.nums[i])
			self.backtrack(i+1)
			self.auxarr.pop()
	
	def subsets(self, nums: List[int]) -> List[List[int]]:
		self.n = len(nums)
		self.nums = nums
		startindex = 0
		
		self.backtrack(startindex)
		return self.result