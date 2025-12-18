# Last updated: 18/12/2025, 20:19:14
class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        sign = +1

        stack = []
        result = 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch =="+" :
                result += sign * num
                num = 0
                sign = +1
            elif ch == "-":
                result += sign * num
                num = 0
                sign = -1
            elif ch == "(":
                stack.append(result)
                stack.append(sign)
                sign = +1
                result = 0
            elif ch == ")":
                result += sign * num
                sgn = stack.pop()
                prev = stack.pop()

                result = sgn * result + prev
                num = 0
        return result + sign * num
