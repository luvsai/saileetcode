# Last updated: 18/12/2025, 20:16:47
from typing import List
class Solution: 
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]: 
        survivingrobos = []
        sortedrobos = []
        for i in range(len(positions)) :
            #(position, health, direction, roboindex)
            sortedrobos.append([positions[i],healths[i], directions[i], i+1])
        # print(sortedrobos)
        sortedrobos.sort(key = lambda x: x[0])
        # print(sortedrobos)
        st = []
        for i in range(len(sortedrobos)):
            robo = sortedrobos[i]
            if robo[2] == "R":
                st.append(robo)
                # print(st)
            else:
                while len(st) != 0:
                    robo_st = st[-1]
                    # fight
                    if robo[1] == robo_st[1]:
                        robo_st[1] = 0
                        robo[1] = 0
                        st.pop()
                        break
                    if robo[1] > robo_st[1] :
                        robo_st[1] = 0
                        st.pop()
                        # print(st)
                        robo[1] -= 1
                    else :
                        robo[1] = 0
                        robo_st[1] -=1
                        break
                if robo[1] > 0:
                    survivingrobos.append(robo)
        for robo in st:
            survivingrobos.append(robo)
        survivingrobos.sort(key = lambda x : x[-1])
        
        finalhealths = [_[1] for _ in survivingrobos ]
        return finalhealths
