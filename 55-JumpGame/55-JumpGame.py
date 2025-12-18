# Last updated: 18/12/2025, 20:20:50
class Solution:
	def canJump(self, nums: List[int]) -> bool:
		#O(n2 and TLE) 17 secs
		# n = len(nums)
		# canreachmem = [-1] * n
		# def canreach(step):
		# 	if step >= n:
		# 		return False
		# 	if canreachmem[step] != -1:
		# 		return canreachmem[step]
		# 	if step == n-1:
		# 		return True
		# 	curjumph = nums[step]
		# 	for i in range(1, curjumph + 1):
		# 		if canreach(step + i):
		# 			canreachmem[step] = True
		# 			return True
		# 	return False
		# return canreach(0) 

		#o(n) solution with 1 sec
		farthestindex = 0
		n = len(nums)
		lastindex = n-1
		for i in range(n):
			currfarthestindex = i + nums[i]
			if farthestindex >= i:
				farthestindex = max(farthestindex, currfarthestindex)
				if farthestindex >= lastindex:
					return True
			else:
				return False
		return False	  
		