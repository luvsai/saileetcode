# Last updated: 18/12/2025, 20:18:23
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        ## name the problem
        # dp[i][j] holds the maximum leng of longes palindrom seq,
        #  can be crated using character betweeen indices i and j (indices included)
        # dp[i][j] holds the value in integers.

        ## transition / recuurence

        # if s[i] == s[j]:
           # dp[i][j] = 2 + dp[i +1 ][j-1]
        
        # else:
        #   dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        ###  base condition are same if if s[i] == s[j]: and length of sequence is <=3 length of dp[i][j] = j-i + 1 or length

        ### order of computation
        # we do tha computation form smaller length to larger
        # 
        # 
        n = len(s)
        
        dp = [[0]* n for _ in range(n)]
        for length in range(1,n + 1):
            for i in range(n - length + 1):
                j  = i + length -1
                if s[i] == s[j]:
                    if length <= 3:
                        dp[i][j] = length
                    else:
                        dp[i][j] = 2 + dp[i+1][j-1]
                    
                else:
                    dp[i][j] = 0 + max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]

        
