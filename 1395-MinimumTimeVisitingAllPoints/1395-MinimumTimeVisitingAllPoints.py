# Last updated: 08/01/2026, 19:54:49
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time =0
        for i in range(1, len(points)) :
            x1, y1 = points[i-1]
            x2, y2 = points[i]
            time += max(abs(x2-x1), abs(y2-y1))
        return time