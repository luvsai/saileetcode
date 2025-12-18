# Last updated: 18/12/2025, 20:16:52
from collections import defaultdict
class DetectSquares:
# task 
# a) organize the points when addd is called to have a quick lookup for the points to make a square
#b) a alogrithm to find the squres found using a new point .


#datastrucutures: 
# hashmap : point vs count of points
# hasmap : x corordinate vs list of y coordinates values




    def __init__(self):
        self.countpairs = defaultdict(int)
        self.xypairs = defaultdict(set)

    def add(self, point: List[int]) -> None:
        x,y = point
        self.countpairs[(x,y)] += 1
        self.xypairs [x] .add(y)

    def count(self, point: List[int]) -> int:
        scount = 0
        x, y = point
        for y2 in self.xypairs[x]:
            if y == y2 :
                continue
            
            # side lenght
            side = abs(y2- y)

            # add the side to x coordingate to find the cooradinate towards to right 
            x2 = x + side
            
            scount += self.countpairs[(x2,y)] * self.countpairs[(x2,y2)] * self.countpairs[(x, y2)] 
            # reduce the sice to x coordinate to find the coordinate towards to the left.   
            x2 = x - side
            scount += self.countpairs[(x2,y)] * self.countpairs[(x2,y2)] * self.countpairs[(x, y2)]
        return scount
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)