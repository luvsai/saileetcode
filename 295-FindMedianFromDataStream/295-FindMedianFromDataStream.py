# Last updated: 18/12/2025, 20:18:58
import heapq
class MedianFinder:

    def __init__(self):
        self.small = [] # max-heap (invert values)
        self.large = [] # min-heap

    def addNum(self, num: int) -> None:
        # 3 steps process;
        #1  always push in max-heap
        heapq.heappush(self.small, -num)
        # 2 fix oderinng: if top element of max heap is greater than bottom element of the min heap towards right
        if self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # 3 balance size: max difference 1
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large,val)

        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()