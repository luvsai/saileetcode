# Last updated: 18/12/2025, 20:18:31
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key= lambda x: x[1])

        arrow_count = 1
        n = len(points)
        curr_end = points[0][1]
        for i in range(1 ,n):
            
            baloon = points[i]
            if baloon[0] <= curr_end:
                continue
            else:
                arrow_count +=1
                curr_end = baloon[1]
        return arrow_count

