# Last updated: 18/12/2025, 20:21:12
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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
		# pick 
		for i in range (startindex , self.n):
			if target >= self.nums[i]:
				self.auxarr.append(self.nums[i])
				self. backtrack( i, target - self.nums[i])		
				self.auxarr.pop()


		# if target >= self.nums[startindex]:
		# 	self.auxarr.append(self.nums[startindex])
		# 	self. backtrack( startindex, target - self.nums[startindex])		
		# 	self.auxarr.pop()
			
		# if startindex < (self.n -1) :
		# 	startindex +=1
		# 	self.backtrack( startindex , target)
	

	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		self.nums = candidates
		n = len(self.nums)
		self.n = n
		startindex = 0
		self.backtrack(startindex, target)
		return self.result