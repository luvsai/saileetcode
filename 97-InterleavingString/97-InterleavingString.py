# Last updated: 18/12/2025, 20:20:16
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        # dp = [ [False] * (len(s2) + 1) for _ in range(len(s1 ) + 1)]

        # baseconditions:
        # empty string of s3 with empty string of s1 and s2

        # dp[0][0] = True

    

        # final answer at dp[len(s1), len(s2)]

        # for i in range( len(s1) + 1):
        #     for j in range(len(s2) + 1):
        #         if i>0 and s3[i+j-1] == s1[i-1]:
        #             dp[i][j] |= dp[i-1][j]
        #         if j>0 and s3[i+j-1] == s2[j-1]:
        #             dp[i][j] |= dp[i][j-1]
        # return dp[len(s1) ][len(s2)]


        # optimizing dp
        dpp = [False] * (len(s2) + 1) 
        dpc = [False] * (len(s2) + 1)

        dpc[0] = True
        
        for i in range( len(s1) + 1):
            for j in range(len(s2) + 1):
                if i>0 and s3[i+j-1] == s1[i-1]:
                    dpc[j] |= dpp[j]
                if j>0 and s3[i+j-1] == s2[j-1]:
                    dpc[j] |= dpc[j-1]
            dpp = dpc
            dpc = [False]* (len(s2) + 1)
        return dpp[len(s2)]