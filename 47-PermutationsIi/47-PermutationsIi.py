# Last updated: 18/12/2025, 20:21:00
class Solution:
	def __init__(self):
		self.result = []
		self.auxarr = []
		self.used = []
		self.nums = []
		self.n = 0
	def backtrack(self):
		if len(self.auxarr) == self.n:
			self.result.append(list(self.auxarr))
			return
		for i in range(self.n):
			if not self.used[i]:
				if i > 0 and self.nums[i] == self.nums[i-1] and not self.used[i-1]  :
					continue
				self.used[i] = True
				self.auxarr.append(self.nums[i])
				self.backtrack()
				self.auxarr.pop()
				self.used[i] = False
	def permuteUnique(self, nums: List[int]) -> List[List[int]]:
		self.nums = nums
		self.nums.sort()
		self.n = len(nums)
		self.used = [False] * self.n
		self.backtrack()
		return self.result