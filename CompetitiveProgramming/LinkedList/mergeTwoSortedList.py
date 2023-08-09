# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        newHead =  pointer = ListNode()

        while(list1 and list2):

            if(list1.val < list2.val):
                pointer.next = list1
                list1 = list1.next

            else:
                pointer.next = list2
                list2 = list2.next

            pointer = pointer.next

        pointer.next = list1 or list2

        return newHead.next

        

    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if(list1 == None):
            return list2

        if(list2 == None):
            return list1

        newHead = None


        if(list1.val <= list2.val):
            newHead = list1
            list1 = list1.next

        else:
            newHead = list2
            list2 =list2.next

        newHead.next = None 
        position = newHead 

        while(list1 and list2):

            if(list1.val <= list2.val):
                position.next = list1
                list1 = list1.next

            else:
                position.next = list2
                list2 = list2.next


            position = position.next
            position.next = None

        while(list1):
            position.next = list1
            list1 = list1.next

            position = position.next
            position.next = None


        while(list2):
            position.next = list2
            list2 = list2.next

            position = position.next
            position.next = None

        return newHead




            

    
