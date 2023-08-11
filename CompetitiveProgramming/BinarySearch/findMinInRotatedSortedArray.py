class Solution:

    def findMin(self, nums: List[int]) -> int:

        # Consider the first element as the min element
        minElement = nums[0]

        left = 0 

        right = len(nums)-1

        while(left <= right):

            mid = (left+right)//2

            # if the middle element is greater than or equal to the min Element 
            # There might be elements with lower value on the right due to rotation

            if(minElement <= nums[mid]):

                left = mid + 1
            
            # The array has been rotated such that there might be lower elements on the left 
            else:

                minElement = nums[mid]

                right = mid - 1

        return minElement