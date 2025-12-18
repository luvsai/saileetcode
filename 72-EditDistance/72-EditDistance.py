# Last updated: 18/12/2025, 20:20:37
#Edit Distance

class Solution:
    def __init__(self):
        self.mem = {}
    def dfs(self,i, j, word1, word2):# min no of operations to be performed on word1 to match word1[i:] with word2[j:]

        if i < 0:
            # word 1 is empty, need to insert all chars of word2 [0: j]
            return j +1
        if j < 0:
            # implies we matched all the character in word2 so we delete rest of the characters in word 1
            return i + 1
            
        if (i,j) in self.mem:
            return self.mem[(i,j)]
        minways = float('inf')
        # implies we couldnt match #TOIDO come back here once
        # characters at the index i and j of word1 and word2 are equal
        
        if word1[i] == word2[j]:
            minways = min(minways, self.dfs(i-1,j-1,word1,word2) + 0)
            # no operation so + 0
        else:
            #delete
            minways = min(minways, self.dfs(i-1, j, word1, word2) + 1)
            
            # insert
            minways = min(minways, self.dfs(i,j-1,word1,word2) + 1)
            
            # replace 
            minways = min(minways, self.dfs(i-1, j-1, word1, word2) + 1) 

# operation is +1 
        self.mem[(i,j)] = minways
        return minways




    def minDistance(self, word1: str, word2: str) -> int:
        m , n = len(word1), len(word2)
        
        return self.dfs(m-1, n-1, word1, word2)

        # tabulation
        
        # dp = [[float('inf')] * (n + 1) for _ in range(m+1)]  
        # # base condition 
        # for j in range(n+1):
        #     dp [0][j]  = j 
        # for i in range(m+1):
        #     dp[i][0] = i 
        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         if word1[i-1] == word2[j-1]:
        #             dp[i][j] =  dp[i-1][j-1]
        #             # no operation so + 0
        #         else:
        #             #delete
        #             dp[i][j] = min(dp[i][j], dp[i-1][j], dp[i][j-1], dp[i-1][j-1]  )  + 1
                    
        # return dp[-1][-1]