# Last updated: 08/01/2026, 19:56:30
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # step1 find the middle
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        # slow will be pointing at n//2 + (1 if odd, 0 if even) index ( 9-> 5 8-> 4)

        # now we reverse from next index slow stopped.
        prev = None
        cur = slow.next
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        # step 3 compare the halves

        first = head
        second = prev
        while second:
            if first.val != second.val:
                return False
            first = first .next
            second = second.next
        return True


        