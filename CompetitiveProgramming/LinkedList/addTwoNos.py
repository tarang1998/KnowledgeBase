# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        sumLLHead = ListNode(0,None)

        tempNode = sumLLHead

        # Variable to hold the carryOver value after the summation of the values
        toBeAdded = 0 

        while(l1 != None or l2 != None or toBeAdded != 0):


            # The value from each linked list 
            l1Val = 0 
            l2Val = 0 
            
            if(l1 != None):
                l1Val = l1.val

            if(l2 != None):    
                l2Val = l2.val


            # Assigning the summed up values and calculating the carry over
            summation = l1Val + l2Val + toBeAdded

            toBeAdded = summation // 10 

            tempNode.val = summation % 10 

            # Traversing through the LL
            if(l1 != None):
                l1 = l1.next 

            if(l2 != None):
                l2 = l2.next

            # Creating new node if their are not lefts in either LL or a carry over value
            if(l1 == None and l2 == None and toBeAdded == 0):
                tempNode.next = None 
            else:
                tempNode.next = ListNode(0,None)

            tempNode = tempNode.next

            
            
        return sumLLHead