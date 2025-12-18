# Last updated: 18/12/2025, 20:20:20
# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
class Solution :
	def __init__(self):
		self.auxarr = []
		self.result = []
		self.n = 0
		self.nums = []
	def backtrack(self, startindex ):
		self.result.append(list(self.auxarr))
		
		for i in range(startindex, self.n):
			
			if i > startindex and self.nums[i] == self.nums[i-1]:
				continue
			

			self.auxarr.append(self.nums[i])
			self.backtrack(i+1)
			self.auxarr.pop()
	
	def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
		self.n = len(nums)
		self.nums = nums
		self.nums.sort()
		startindex = 0
		
		self.backtrack(startindex)
		return self.result