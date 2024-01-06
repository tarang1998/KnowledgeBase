# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    # Time Complexity : O(n)
    # Space Complexity : O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        updatedHead = None
        while(head):

            next = head.next
            head.next = updatedHead

            updatedHead = head
            head = next

        return updatedHead


