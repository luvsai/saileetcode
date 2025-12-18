# Last updated: 18/12/2025, 20:18:04
class Solution:
	def countOfAtoms(self, formula: str) -> str:
		import collections

		mainst = [collections.defaultdict(int)]
		i = 0
		n = len(formula)
		try:
			while i < n:
				ch = formula[i]
				# print(ch)
				if ch == "(":
					mainst.append(collections.defaultdict(int))
					i = i + 1
				elif ch == ")":
					# print(mainst)
					top = mainst.pop()
					i += 1
					istart = i
					while i < n and formula[i].isdigit():
						i +=1
					multiple = int(formula[istart: i] or 1)
					for ele, ecount in top.items():
						mainst[-1][ele] += ecount * multiple
					
				else:
					i_start = i
					i += 1
					while i < n and formula[i].islower():
						i += 1
					ele = formula[i_start:i]
					
					i_start = i
					while i < n and formula[i].isdigit():
						i += 1
					multiple = int(formula[i_start:i] or 1)
					
					mainst[-1][ele] += multiple
			pdic = mainst.pop()
			sortedelements = sorted(pdic.items())
			result = ""
			for element, value in sortedelements:
				result += element   
				if value > 1:
					result += str(value)
			return result
		except Exception as e:
			# print(e)
			# print(mainst)
			return formula