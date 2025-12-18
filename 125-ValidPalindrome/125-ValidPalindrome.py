# Last updated: 18/12/2025, 20:19:52
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        n = len(s)
        j = n-1
        while i < j and i < n and j>=0:
            while i < n and not s[i].isalnum() :
                i +=1
            while j >-1 and not s[j].isalnum():
                j -=1
            if i <= j:
                if s[i].lower() != s[j].lower() :
                    return False
            i +=1
            j -=1
        return True
