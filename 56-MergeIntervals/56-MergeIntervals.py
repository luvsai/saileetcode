# Last updated: 18/12/2025, 20:20:48
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        neint = [intervals[0]]
        for i in intervals[1:]:
            if neint[-1][1] >= i[0]:
                neint[-1][1] = max (neint[-1][1], i[1])
            else:
                neint.append(i)

        return neint



            


        