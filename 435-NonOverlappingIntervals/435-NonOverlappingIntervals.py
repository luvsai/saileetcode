# Last updated: 18/12/2025, 20:18:34
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # imagine the intervals represent the meetings start and end time. and two meetings can end with and start on same time.

        # we want to maximize the no of meetings here. so we always priotize the meeting runi short time . minimizing no of failed meetings which take long time interval.
        # approach is sort the meeting with their end time.
        # 
        sorted_intervals = sorted(intervals,key = lambda x : x[1])
        count = 0
        preend = float('-inf')
        for start, end in sorted_intervals:
                if start >= preend:
                    preend = end
                else:
                    count +=1
        return  count







