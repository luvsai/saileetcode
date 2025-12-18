# Last updated: 18/12/2025, 20:16:46
from collections import defaultdict
class Solution:
    def minimumPushes(self,word:str) -> int:
        charactercountdic = defaultdict(int)
        for key in word:
            charactercountdic[key] += 1
        items = list(charactercountdic.items())
        items.sort(key = lambda x: x[1],reverse=True)
        currentkey = 2
        push_count = 1
        min_pushes = 0
        for item in items:
            char_count = item[1]
            min_pushes += char_count * push_count
            if currentkey ==9 :
                currentkey = 2
                push_count +=1
            else :
                currentkey +=1
        return min_pushes