# Last updated: 18/12/2025, 20:18:01
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        answers = [0] * n
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                answers[idx] = i - idx
            stack.append(i)
        return answers
        