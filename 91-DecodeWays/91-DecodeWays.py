# Last updated: 18/12/2025, 20:20:18
class Solution:
    s = ""
    n = 0
    def dfs(self, index):
        if index ==self.n :
            return 1
        if index > self.n:
            return 0
        
        ways  = 0
        if self.s[index] != '0':
            # pick 1 element
            ways += self.dfs(index +1)
            # pick two elements
            # if we are at last but one index 
            if index < self.n-1 and int(self.s[index: index+2]) <= 26 :
                ways += self.dfs(index + 2)
        
        return ways
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        
        # dynamic programming.
        # dp [index] = no ways string starting at index to the length of the arrya can be decoded .
        # base condition : dp[n] = 1
        dp[n] =1
        for i in range(n-1, -1, -1):
            if s[i] != '0' :
                #pick single letter:
                dp [i] += dp[i+1]
                #pick two leteters
                if i < n-1 and int(s[i: i+2]) <=26:
                    dp[i] += dp[i+2]
                
        return dp[0]