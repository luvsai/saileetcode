# Last updated: 18/12/2025, 20:20:38
class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')

        stack = []
        for part in parts:
            if part == "" or part == "." :
                continue
            elif part == "..":
                if stack :
                    stack.pop()
            else:
                # valid directory name 
                stack.append(part)
        return "/" + "/".join(stack)