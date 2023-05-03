class Solution:

    def trap(self, height: List[int]) -> int:

        n = len(height)

        maxLeftHeight = height[0]

        maxRightHeight = height[n-1]

        left = 1

        right = n-2

        totalArea = 0 

        while(left <= right):

            if(maxLeftHeight < maxRightHeight):

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

                    

