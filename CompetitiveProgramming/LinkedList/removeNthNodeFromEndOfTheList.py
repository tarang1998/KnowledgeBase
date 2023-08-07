# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Let variable act as a queue capable of holding n+1 elements at a time 
        queue = []

        pointer = head 

        # Storing the last n+1 elements in the queue
        while(pointer):

            if(len(queue) < n+1):

                queue.append(pointer)

            else:
                queue.pop(0)
                queue.append(pointer)

            
            pointer = pointer.next

        # If  n elements in the queue
        # The first element needs to be removed 
        if(len(queue) == n):
            
            return head.next

        # Remove the n the element from the end   
        else:

            queue[0].next = queue[1].next
            return head
