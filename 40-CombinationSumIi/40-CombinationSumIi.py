# Last updated: 18/12/2025, 20:21:10
class Solution:
	def __init__(self):
		self.auxarr = []
		self.result = []
		self.n = 0
	
	def backtrack(self, startindex , target ):
		if target == 0:
			self.result.append(list(self.auxarr))
		if target < 0:
			return 
		
		#pick
		for i in range (startindex , self.n):
			if target >= self.nums[i]:
				if i > startindex and self.nums[i] == self.nums[i-1] :
					continue
				self.auxarr.append(self.nums[i])
				self.backtrack( i+1, target - self.nums[i])		# check this since we only consider the element once we skip to the next one. else i stay at same element.
				self.auxarr.pop()


		# if target >= self.nums[startindex]:
		# 	self.auxarr.append(self.nums[startindex])
		# 	self. backtrack( startindex, target - self.nums[startindex])		
		# 	self.auxarr.pop()
			
		# if startindex < (self.n -1) :
		# 	startindex +=1
		# 	self.backtrack( startindex , target)
	

	def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
		self.nums = candidates
		self.nums.sort()
		n = len(self.nums)
		self.n = n
		startindex = 0
		self.backtrack(startindex, target)
		return self.result