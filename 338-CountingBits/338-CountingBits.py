# Last updated: 18/12/2025, 20:18:44
class Solution:
    def countBits(self, n: int) -> List[int]:
        # ans = []
        # for i in range(n+1) :
        #     count = 0
        #     num = i
        #     while num >0:
        #         count += num & 1
        #         num >>= 1
        #     ans.append(count)
        # return ans

        dp = [0] * (n+1)
        for i in range(1, n+1 ):
            dp[i] = dp[ i >> 1]+ (i & 1)
        return dp
            