# Last updated: 18/12/2025, 20:21:20
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []
        openp = mapping.values()
        for ch in s:
            if ch in openp:
                stack.append(ch)
                continue
            if len(stack) ==0:
                return False
            if mapping[ch] != stack[-1]:
                return False
            stack.pop()
        if len(stack) >0:
            return False
        return True