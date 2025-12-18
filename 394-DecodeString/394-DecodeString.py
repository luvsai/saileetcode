# Last updated: 18/12/2025, 20:18:42
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ""
        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == "[":
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif ch == "]" :
                tple = stack.pop()
                curr_str = tple[0] + curr_str * tple[1]
            else:
                curr_str += ch
        return curr_str
        