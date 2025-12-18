# Last updated: 18/12/2025, 20:20:32
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count  = Counter (t)
        required = len(t_count)
        currcounter = defaultdict(int)
        formed = 0
        left , right = 0,0
        ans = float('inf') ,  left, right
        
        while right < len(s):
            character = s[right]
            
            if character in t_count:
                currcounter[character] +=1
                if currcounter[character] == t_count[character]:
                    formed +=1
            while left <= right and formed == required:
                character = s[left]
                #save the lenght of the current string before we remove
                if right - left + 1 < ans[0]:
                    ans = right - left + 1, left , right    

                if character in t_count:
                    currcounter[character] -=1
                    if currcounter[character] < t_count[character]:
                        formed -=1
                left +=1
            right +=1

        return s[ans[1]: ans[2] + 1] if ans[0] != float('inf') else ""
