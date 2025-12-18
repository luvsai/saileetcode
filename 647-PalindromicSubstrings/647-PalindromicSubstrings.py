# Last updated: 18/12/2025, 20:18:12
class Solution:
    def countSubstrings(self, s: str) -> int:

        # brute force is find all substrings of O(n2). complextiy and for each substring find if the substring is a palindrome.
        # O(n3)
        #dp [i][j] substring starting from i to j including index values is a palindrome or not values (True or False)
        #trasitions; how
        # dp[i][j] is true if s[i] and s[j] are equal and dp[i+1][j-1] is a palindrome.

        #base conditions:
        # if strings of length 1 are palindromes. and strings of length <=3 are palindromes if s[i]==s[j]:

        #order of computation; we try to fill in from lenght 1 strings to length n
        # at every computation we would increment count if dp[i][j] is True
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        count = 0

        for length in range(1, n +1):
            for i in range(n-length + 1):
                j  = i + length -1 # j index is also included
                if s[i] == s[j]:
                    if length <=3:
                        dp[i][j] = True
                        count +=1
                    elif dp[i+1][j-1]:
                        dp[i][j]  = True
                        count +=1
        return count     