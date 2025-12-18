# Last updated: 18/12/2025, 20:18:43
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for item , count in freq.items():
            heapq.heappush(heap,(count,item))
            if len(heap) > k:
                heapq.heappop(heap)
        return [value for (count, value) in heap]
