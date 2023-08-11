

class Solution:

    def findDuplicate(self, nums: List[int]) -> int:

        slow = nums[0]
        fast = nums[nums[0]]

        #The Linked List in this case would always have a cycle 
        #Due to the conditions len(nums) == n+ 1 and 1<=num[1]<=n (atleast one element would be repeated)
        #Store the intersection where the first pointer and the second pointer
        #The intersected point would be the start of the cycle 
        while(slow != fast):
            slow = nums[slow]
            fast = nums[nums[fast]]


        slow = 0 

        #To find the duplicated value in the array 
        #The distance betwwen the intersection and the duplicated node 
        #is equal to the distance between the start and the duplicated node
        while(slow != fast):
            slow = nums[slow]
            fast = nums[fast]

        return slow
        






        
