# Last updated: 18/12/2025, 20:18:28
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        i = 0
        j = 0
        ctr = 0
        while i<len(g) and j < len(s):
            if g[i] <= s[j]:
                ctr +=1
                i +=1
                j +=1
            else:
                j +=1

        return ctr