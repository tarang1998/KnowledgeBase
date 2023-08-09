

class Solution:

    def findDuplicate(self, nums: List[int]) -> int:

        slow = nums[0]
        fast = nums[nums[0]]

        #Loop to find the cycle in the LL
        #And store where the first pointer and the second pointer meet 
        while(slow != fast):
            slow = nums[slow]
            fast = nums[nums[fast]]


        slow = 0 

        # To find the duplicated no
        while(slow != fast):
            slow = nums[slow]
            fast = nums[fast]

        return slow
        






        
