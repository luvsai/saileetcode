# Last updated: 18/12/2025, 20:19:44
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        mem = {}

        def dfs(start):
            if start == len(s):
                return True
            if start in mem:
                return mem[start]
            for end in range(start+1, len(s) +1):
                if s[start:end] in word_set and dfs(end):
                    mem[start] = True
                    return True
            mem[start] = False
            return False
        return dfs(0)