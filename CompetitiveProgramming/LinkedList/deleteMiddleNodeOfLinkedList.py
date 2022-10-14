# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        firstPointer = head 
        secondPointer = head 

        if(firstPointer.next == None):
            return None

        if(firstPointer.next.next == None):
            head.next = None
            return head

        while(secondPointer!= None and secondPointer.next != None):

            firstPointer = firstPointer.next

            secondPointer = secondPointer.next.next

                  
        firstPointer.val = firstPointer.next.val
        firstPointer.next = firstPointer.next.next

        return head

