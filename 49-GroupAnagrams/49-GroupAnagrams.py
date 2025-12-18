# Last updated: 18/12/2025, 20:20:56
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] +=1
            key = tuple(freq)
            groups[key].append(word)
        return list(groups.values())