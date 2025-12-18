# Last updated: 18/12/2025, 20:19:40
class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        currstr = ""
        i = 0
        n = len(s)
        while i < n :
            if s[i] == " ":
                i +=1
                continue
            else:
                while i < n and s[i] != " ":
                    currstr += s[i]
                    i +=1
                stack.append(currstr)
                currstr = ""
            
        reversestr = ""
        while stack:
            word = stack.pop()
            reversestr += word
            if stack:
                reversestr += " "
        return reversestr


        