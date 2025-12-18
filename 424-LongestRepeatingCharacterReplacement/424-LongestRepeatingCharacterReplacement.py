# Last updated: 18/12/2025, 20:18:35
class Solution:
    # TODO comeback
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26

        farraysum = 0

        left , right = 0,0
        longestsubstr = 0
        maxcharidx = 0
        for right in range(len(s)):

            char = s[right] 
            charidx = ord(char) - ord('A')
            freq [ charidx] +=1
            farraysum +=1
            if freq[charidx] > freq[maxcharidx] :
                maxcharidx = charidx
            while (farraysum - freq[maxcharidx] ) > k:
                charl = s[left]
                charlidx = ord(charl) - ord('A')
                freq[charlidx] -=1 
                farraysum -=1
                
                for cidx, f in enumerate(freq): #O(26)
                    if  f > freq[maxcharidx]:
                        maxcharidx = cidx
                left +=1
                


            longestsubstr = max(longestsubstr, right - left + 1)
        return longestsubstr
            