# Last updated: 18/12/2025, 20:21:05
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #dp[i][j]
        
        m = len(s) + 1
        n = len(p) + 1
        dp = [[False] * n for _ in range(m)]

        ##base conditions
        dp[0][0] = True  

        # matching an empty string s[:0] with with p[:j] 
        # dp[0][j] = True if p[j - 1] == "*" and dp[0][j-1]
        for j in range(1,n):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-1]


        for i in range(1,m ):
            for j in range(1,n ):
                if p[j - 1] == "?" or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*" :
                    # take empty value for * and move back for p [:j]
                    val1 = dp[i][j-1] 
                    # take a character and match with s[i-1]and move s[:i] to one step back
                    val2 = dp[i-1][j]
                    dp[i][j] = val1 or val2

#        print(dp)
        return dp[-1][-1]