# Last updated: 18/12/2025, 20:19:20
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nrange =   range(numCourses)
        adjlist = [[] for _ in nrange]
        # [i,j] => there is edge from i to j
        indeg = [0 ] * numCourses
        for pre in prerequisites:
            i = pre[0]
            j = pre[1]
            adjlist[j].append(i)
            indeg[i] +=1
        
        q = deque([])

        for course in nrange:
            if indeg[course] == 0:
                q.append(course)
        courseorder = [] 
        while q:
            course = q.popleft()
            courseorder.append(course)
            for neighbor in adjlist[course]:
                indeg[neighbor] -= 1
                if indeg[neighbor] == 0:
                    q.append(neighbor)
        if len(courseorder) == numCourses:
            return courseorder
        return []