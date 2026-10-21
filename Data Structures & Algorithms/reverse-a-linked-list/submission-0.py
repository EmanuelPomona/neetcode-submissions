# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            ##temp = current.next
                ## remove temp = current.next because at the very end of the singly linked list, we land/end on a non-existent node, so we can't reassign temp as current.next if current doesn't exist.

        return prev
        


        