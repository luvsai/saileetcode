# Last updated: 08/01/2026, 19:56:10
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # algo basically we maintain a monotonically increasing. stack .
        # if a digiton top of stack  is bigger than next digit and if we have removals left from k removals
        # we replace the top of stack with the new digit. if k i exhausted we append the value 

        stack = []
        for ch in num:
            while stack and stack[-1] > ch and k>0:
                k -=1
                stack.pop()
            if not stack and ch == '0': # if stack is empty and 0 to be appended we kind of not need it and reduce the no of digits in the ifnal stack
                continue
            stack.append(ch)

        while k>0 and stack: # mandatory to remove k character and removing stack is monotonous removing end would result in samll whole result
            stack .pop()
            k -=1
        if not stack: # order after done with stack operations check if stack still have value
            return '0'
        return "".join(stack)
        
        