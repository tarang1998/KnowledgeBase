# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        updatedHead = None

        while(head):

            next = head.next
            head.next = updatedHead

            updatedHead = head
            head = next

        return updatedHead    
        
    def reorderList(self, head: Optional[ListNode]) -> None:

        #Traverse through the linked list to find the middle and end of the linked list
        first_pointer = head 
        second_pointer = head

        while(second_pointer.next != None and second_pointer.next.next != None):

            first_pointer = first_pointer.next
            second_pointer = second_pointer.next.next


        #Divide the linked list in two parts 
        second_ll_head = first_pointer.next
        first_pointer.next = None


        #Reverse the second linked list 
        second_head = self.reverseList(second_ll_head)

        #Reorder the two linked list 
        first_node = head
        second_node = second_head

        while(first_node != None and second_node != None ):

            temp_first = first_node.next
            first_node.next = second_node
            first_node = temp_first
            temp_second = second_node.next
            second_node.next = first_node
            second_node = temp_second

        return head





      



        

        




        