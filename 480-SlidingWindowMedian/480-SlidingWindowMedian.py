# Last updated: 18/12/2025, 20:18:29
import heapq
from collections import defaultdict
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small = []   # max heap (negated)
        large = []   # min heap
        delayed = defaultdict(int)
        
        small_size = 0
        large_size = 0

        def prune(heap):
            while heap:
                num = -heap[0] if heap is small else heap[0]
                if delayed[num] > 0:
                    delayed[num] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def balance():
            nonlocal small_size, large_size
            
            if small_size > large_size + 1:
                prune(small)
                heapq.heappush(large, -heapq.heappop(small))
                small_size -= 1
                large_size += 1
                prune(small) # Keep top clean
                
            elif small_size < large_size:
                prune(large)
                heapq.heappush(small, -heapq.heappop(large))
                large_size -= 1
                small_size += 1
                prune(large) # Keep top clean

        def insert(num):
            nonlocal small_size, large_size
            if not small or num <= -small[0]:
                heapq.heappush(small, -num)
                small_size += 1
            else:
                heapq.heappush(large, num)
                large_size += 1
            balance()

        def remove(num):
            nonlocal small_size, large_size
            delayed[num] += 1
            
            # Identify which heap the element effectively belongs to
            if small and num <= -small[0]:
                small_size -= 1
                # CRITICAL FIX: If the element is at the top, prune immediately
                # to ensure we remove it from SMALL, not accidentally from LARGE later.
                if num == -small[0]:
                    prune(small)
            else:
                large_size -= 1
                if large and num == large[0]:
                    prune(large)
            
            balance()

        def get_median():
            prune(small)
            prune(large)

            if k % 2 == 1:
                return float(-small[0])
            else:
                return (-small[0] + large[0]) / 2.0

        res = []
        for i in range(len(nums)):
            insert(nums[i])
            if i >= k:
                remove(nums[i - k])
            if i >= k - 1:
                res.append(get_median())

        return res