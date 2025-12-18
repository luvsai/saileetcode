# Last updated: 18/12/2025, 20:19:41
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-/*":
                stack.append(int(token))
            else:
                y = stack.pop()
                x = stack.pop()
                val = None
                if token == "+":
                    val = x + y
                elif token == "-":
                    val = x - y
                elif token == '*':
                    val = x * y
                elif token == "/":
                    val = int(x / y)
                stack.append(val)
        return stack[-1]
        