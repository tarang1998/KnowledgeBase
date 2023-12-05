# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    # Time Complexity : O(n.logk)
    # Where n is the total no of elements in all the list    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None

        while(len(lists)>1):

            mergeList = []


            for i in range(0,len(lists),2):
                l1 = lists[i]

                l2 = None

                if(i+1 < len(lists)):
                    l2 = lists[i+1] 

                mergeList.append(self.mergeLL(l1,l2))

            lists = mergeList

        return lists[0]


    def mergeLL(self,l1,l2):


        pointer =  ListNode()
        head = pointer

        while(l1 != None and l2 != None):

            if(l1.val < l2.val):
                pointer.next = l1
                l1 = l1.next

            else:
                pointer.next = l2
                l2 = l2.next

            pointer = pointer.next
            pointer.next = None 

        
        if(l1 == None):
            pointer.next = l2
        else:
            pointer.next = l1

        return head.next
        