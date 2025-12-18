# Last updated: 18/12/2025, 20:19:03
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        freq1 = [0] * 26
        for ch in s:
            freq1[ord(ch) - ord('a')] +=1
        freq2 = [0] * 26
        for ch in t:
            freq2[ord(ch) - ord('a')] +=1
        key1 = tuple(freq1)
        key2 = tuple(freq2)
        if key1 == key2:
            return True
        else:
            return False

        