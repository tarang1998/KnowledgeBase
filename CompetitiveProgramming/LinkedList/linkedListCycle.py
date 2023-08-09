# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # Time Complexity : O(n), Space Complexity : O(1)
    # Floyds Cycle-Finding Algorithm
    # Move slow pointer by 1 and fast pointer by 2 
    # If the pointers meet at some node then there is a loop
    # Else no loop present 
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slowPointer = head 
        fastPointer = head
        
        while(fastPointer and fastPointer.next):
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

            if(slowPointer == fastPointer):
                return True 

        return False 

    # Time Complexity : O(n), Space Complexity : O(n)
    def hasCycle2(self, head: Optional[ListNode]) -> bool:

        # Dictionary to store all the visited nodes
        visitedNodes = {}

        while(head):

            if(head in visitedNodes):
                return True

            visitedNodes[head] = 1

            head = head.next 

        return False

    # Time Complexity : O(n), Space Complexity : O(1)
    def hasCycle3(self, head: Optional[ListNode]) -> bool:


        while(head):

            if(head.val == 1000000):
                return True

            head.val = 1000000

            head = head.next 

        return False