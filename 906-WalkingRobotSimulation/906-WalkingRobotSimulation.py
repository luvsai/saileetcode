# Last updated: 18/12/2025, 20:17:36
import math
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [0,1,2,3] # N ,E,  S, W # +y, +x, -y, -x
        current_direction = 0 
        current_pos = [0,0] # (x,y)
        obset = set([(x[0],x[1]) for x in obstacles]) 
        newpos_pos = [0,0]
        mdfo = 0
        for command in commands:
            #change direction
            if command == -2:
                current_direction = current_direction - 1 
                if current_direction == -1:
                    current_direction = 3
            elif command == -1 :
                current_direction = (current_direction + 1) % 4
            else :
                # distance = command
                newpos_pos = current_pos[:]
                for _ in range(command):

                    if current_direction == 0:

                        newpos_pos [1] += 1

                    elif current_direction == 1:
                        newpos_pos [0] += 1
                    elif current_direction == 2:
                        newpos_pos [1] -= 1
                    else :
                        newpos_pos [0] -= 1
                    
                    # we need to check if we want to move to new position or not
                    if (newpos_pos[0],newpos_pos[1]) not in obset:
                        current_pos = newpos_pos[:]
                    else:
                        break
                sq = int(math.pow(current_pos[0],2) + math.pow(current_pos[1],2))
                mdfo = max(mdfo,sq)

        #sq = math.pow(current_pos[0],2) + math.pow(current_pos[1],2)
        return mdfo