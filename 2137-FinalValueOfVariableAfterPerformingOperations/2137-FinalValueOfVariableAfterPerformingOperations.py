# Last updated: 18/12/2025, 20:16:54
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for operation in operations:
            if '+' in operation:
                x +=1
            else:
                x -=1
        return x