# Last updated: 22/12/2025, 19:27:00
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        stack2 = []
        for ch in s:
            if ch == "#":
                if stack :
                    stack.pop()
            else:
                stack.append(ch)
        for ch in t:
            if ch == "#":
                if stack2 :
                    stack2.pop()
            else:
                stack2.append(ch)
        if len(stack) != len(stack2):
            return False
        for (x,y) in zip(stack, stack2):
            if x != y:
                return False
        return True

