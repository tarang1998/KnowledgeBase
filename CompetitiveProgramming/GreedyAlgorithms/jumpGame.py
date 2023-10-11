
class Solution:


    # Time Complexity : O(n)
    def canJump(self, nums: List[int]) -> bool :

        dest = len(nums)-1

        for i in range(len(nums)-2,-1,-1):

            # Shift the dest to the index 
            # If the dest can be reached from the ith index 
            # given nums[i] steps
            if(i + nums[i] >= dest):

                dest = i

        return True if dest == 0 else  False

                








        