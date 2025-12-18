# Last updated: 18/12/2025, 20:21:22
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        for i in range(n-1):
            if fast.next:
                fast = fast.next
            else:
                break
        pr = dummy
        while fast.next :
            fast = fast.next
            pr = slow
            slow= slow.next
        
        pr.next = slow.next
        return dummy.next
        

