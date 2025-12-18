# Last updated: 18/12/2025, 20:19:24
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        previous = None
        while curr :
            nextnode = curr.next
            curr.next = previous
            previous = curr
            curr = nextnode
            
        return previous
        