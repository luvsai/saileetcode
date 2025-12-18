# Last updated: 18/12/2025, 20:21:17
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #kway merge using heap
        # insert stage
        heap = []
        tail = None
        final = []
        head = None
        for i  in range(len(lists)):
            if not lists[i]:
                continue
            llnode = lists[i]
            heapq.heappush(heap, (llnode.val, i, llnode))
        while heap:
            llntuple = heapq.heappop(heap)
            if not head:
                head = llntuple[2]
            if tail:
                tail.next = llntuple[2]
            tail = llntuple[2]
            
            if llntuple[2].next:
                nextnode = llntuple[2].next
                heapq.heappush(heap, (nextnode.val, llntuple[1], nextnode ))  
        return head          




        #remove and insert until the heap is empty
        