class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)

        # The missing positive integer here must be in the range : [1,n+1]

        # Keep a record if the array contains 1
        containsOne = 0

        # Convert all the element >=n+1 or <=0 to 1
        for i in range(n):

            if nums[i] == 1:
                containsOne = 1 
                continue

            if nums[i] <= 0 or nums[i]>= n+1:
                nums[i] = 1 
        
        # Check if the array contains one, if not return 1
        if containsOne == 0:
            return 1 


        # loop through the array, to mark the elements existing in the range [1,n+1], if element exist, make the num at (index = element-1) as negative
        # if element = 1 , mark element at index = 0 as -ve
        for i in range(n):
            ele = abs(nums[i])
            index = ele-1
            nums[index] = -1 * abs(nums[index])

        # loop the array to find the missing positive number
        for i in range(n):
            if nums[i]>0:
                return i+1

        return n+1


        


        