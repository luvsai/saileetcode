# Last updated: 18/12/2025, 20:19:11
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        last_op = '+'
        for i , ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            
            # if operator or end of the string
            if ch in '+-*/' or (i == len(s) -1):
                if last_op == '+':
                    stack.append(num)
                elif last_op == '-':
                    stack.append(-num)
                elif last_op =='*':
                    stack.append(num * stack.pop())
                elif last_op =='/':
                    prev = stack.pop()
                    stack.append(int(prev/num))
                last_op = ch
                num = 0
        return sum(stack)
