# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    # Time Complexity : O(n)
    # Space Complexity : O(1) 
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head 

        # Find the middle element of the linked list 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        # Reverse the second half of the linked list to point to slow 
        prev = slow
        slow = slow.next
        # Break the cycle to prevent an endless loop with the second half 
        prev.next = None
       
        while(slow):
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Compare the first half and the reversed second half 
        while prev:
            if prev.val != head.val:
                return False
            
            head = head.next 
            prev = prev.next

        return True 

    
        
    
    # Time Complexity : O(n)
    # Space Complexity : O(1)
    def isPalindrome1(self, head: Optional[ListNode]) -> bool:
        
        ele = []
        
        while head != None:
            ele.append(head.val)
            head = head.next
            
        if ele == ele[::-1]:
            return True
        else: 
            return False

   
        