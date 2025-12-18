# Last updated: 18/12/2025, 20:17:38
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        keys = set()
        m = len(grid) ; n = len(grid[0])
        start = None
        for i in range(m):
            for j in range(n):
                if grid[i][j].islower() :
                    keys.add(grid[i][j])
                if grid[i][j] == '@':
                    start = (i,j)
        finalmask = (1 << len(keys)) -1

        # deque holds the state(index tuple and bitmask) and distance
        q = deque() 
        q.append((start[0],start[1], 0, 0)) #(start[0],start[1], mask, distance))

        #datastructrue 
        #1 bfs state with index tuple and bitmask 
        
        bfsstate = set()
        bfsstate .add(((start[0],start[1]),  0))
        #door_visited = set() # we dont need this since our goal is to acquire all keys.
        # print(bin(finalmask))a
        
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while q:
            x, y, mask , d = q.popleft()

            if mask == finalmask:
                return d
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                newmask = mask
                if 0<= nx< m and 0<=ny < n:
                    # wall
                    if grid[nx][ny] == '#':
                        continue
                    #key
                    if grid[nx][ny].islower() :
                        key = grid[nx][ny]
                        keyindex = ord(key) - ord('a')
                        newmask |= 1 << keyindex

                    #lock
                    #check if keyexitst
                    if grid[nx][ny].isupper() :
                        lock = grid[nx][ny]
                        lockindex = ord(lock) - ord('A')
                        if not (newmask & (1 << lockindex)) :
                            continue
                    #passage '.'

                    if ((nx,ny) , newmask) not in bfsstate:
                        bfsstate.add( ((nx,ny) , newmask) )
                        q.append( (nx, ny, newmask, d+1))
        return -1