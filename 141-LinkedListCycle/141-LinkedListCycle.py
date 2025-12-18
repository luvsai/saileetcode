# Last updated: 18/12/2025, 20:19:43
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head
        flag = False
        while fast and fast.next :
            
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
        return False