# Last updated: 18/12/2025, 20:19:23
from typing import List

from queue import Queue
class Solution:
	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		adj = [list() for i in range(numCourses)]
#calculate the indegrees
		indeg = [0] * numCourses
		for item in prerequisites:
			adj[item[1]].append(item[0])
			indeg[item[0]] +=1
		#get the nodes which are having indegree 0 and put them in q
		q = Queue()
		index = 0
		for val in indeg:
			if val == 0 :
				q.put(index)
			index += 1
		#ts = [] 
		ctr =0
		while not q.empty():
			current_course = q.get()
			#ts.append(current_course)
			ctr +=1
	#check the succeeding courses, can be taken after course
			for course in adj[current_course]:
				indeg[course] -= 1
				if indeg[course] == 0:
					q.put(course)
		if ctr < numCourses:
			return False
		else :
			return True