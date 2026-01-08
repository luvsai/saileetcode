# Last updated: 08/01/2026, 19:56:12
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key= lambda x: (x[0] ,-x[1]))
        if not envelopes :
            return 0
        # envelopes with same width cannot stack up this is contrast to stack is boxes 


        n = len(envelopes)

        lis = []

        for _ , h in envelopes:
            idx = bisect.bisect_left(lis, h)
            if idx == len(lis):
                lis.append(h)
            else:
                lis[idx] = h
        return len(lis)









        # dp = [1] * n

        # #base conditions
        # dp[0] = 1 # first envelope can only exist by itself
        # max_count = 1
        # for i in range(1,n):
        #     for k in range(i):
        #         if ( envelopes[i][0] > envelopes[k][0]) and (envelopes[i][1] > envelopes[k][1]):
        #             dp[i] = max(1 + dp[k] , dp[i])
        #     max_count = max(max_count, dp[i])
        # return max_count