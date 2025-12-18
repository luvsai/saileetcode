# Last updated: 18/12/2025, 20:17:57
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        start = "0000"
        if start in dead:
            return -1
        q = deque()
        q.append((start, 0))
        visited = set()
        visited.add(start)

        while q:
            lock, steps = q.popleft()
            if lock == target:
                return steps
            for i in range(4):
                digit = int(lock[i])

                #rotate up 
                up = (digit + 1)%10
                down = (digit -1 ) % 10

                # form new strings
                next1 = lock[:i] + str(up) + lock[i +1: ]
                next2 = lock[:i] + str(down) + lock[i+1: ]

                for nxt in (next1, next2):
                    if nxt not in visited and nxt not in dead:
                        visited.add(nxt)
                        q.append((nxt, steps + 1))



        return -1
