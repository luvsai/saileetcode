# Last updated: 22/12/2025, 19:26:44
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Sort by length → DP[word] = best predecessor + 1 → delete one char to find parents.
        words.sort(key = lambda x: len(x))
        dp = {}

        for word in words:
            dp[word] = 1
            for i in range(len(word)): #O(L)
                pred = word[:i] + word[i+1:] #O(L)
                if pred in dp:
                    dp[word] = max(dp[word], dp[pred] + 1)
        return max(dp.values())
