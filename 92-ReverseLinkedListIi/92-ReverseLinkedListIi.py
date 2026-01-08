# Last updated: 08/01/2026, 19:57:38
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Algorithm Breakdown

# Create dummy → dummy.next = head
# Move prev to node before left
# curr = prev.next
# Reverse sublist using head insertion technique
# Reconnect pointers
# Return dummy.next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left -1):
            prev = prev.next
        curr = prev.next

        for _ in range(right -left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next