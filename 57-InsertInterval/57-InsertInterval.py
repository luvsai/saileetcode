# Last updated: 18/12/2025, 20:20:46
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # find the position where we can insert the new interval. 
        if not intervals:
            return [newInterval]
        n = len(intervals)
        pos = 0
        final = []
        flag = False
        for i in range( n):
            if not flag:
                if intervals[i][0] > newInterval[0]:
                    if not final:
                        final.append(newInterval)
                    else:
                        # we merge the new interval with the end of the final
                        if newInterval[0] <= final[-1][1]:
                            final[-1][1] = max( newInterval[1], final[-1][1])
                        else:
                            final.append(newInterval)
                    # set flag
                    flag = True

            if not final :
                final.append(intervals[i])
            else:
                if intervals[i][0] <= final[-1][1]:
                    final[-1][1]  = max(intervals[i][1], final[-1][1]) 
                else:
                    final.append(intervals[i])
        if not flag:
            # we merge the new interval with the end of the final
            if newInterval[0] <= final[-1][1]:
                final[-1][1] = max( newInterval[1], final[-1][1])
            else:
                final.append(newInterval)

        return final
            