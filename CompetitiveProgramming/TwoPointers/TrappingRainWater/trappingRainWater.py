class Solution:

    # Time Complexity : O(n)
    # Space Complexity : O(1)

    def trap(self, height: List[int]) -> int:

        n = len(height)

        maxLeftHeight = height[0]

        maxRightHeight = height[n-1]

        left = 1

        right = n-2

        totalArea = 0 


        # loop until the left and the right pointers meet  
        while(left <= right):

            # At a certain point the amount of water than can be stored
            # depends on the lower boundary height 
            # and it doesnt matter how height the other boundary is 
            if(maxLeftHeight < maxRightHeight):


                # If the max height is greater only then there is a possibility to trap water 
                # else we need to update the max height
                if(maxLeftHeight > height[left]):

                    totalArea += maxLeftHeight - height[left]

                else:

                    maxLeftHeight = height[left]

                left += 1 
            
            else :

                if(maxRightHeight > height[right]):

                    totalArea += maxRightHeight - height[right]

                else :

                    maxRightHeight = height[right]

                right -= 1

        return totalArea

                    

