# Last updated: 18/12/2025, 20:17:35
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        flag = False
        while fast.next :
            fast = fast.next
            if not flag:
                flag = True
            else:
                flag = False
                slow = slow.next
        if flag:
            return slow.next
        return slow
