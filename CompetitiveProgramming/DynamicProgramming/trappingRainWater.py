class Solution:

    # Time Complexity : O(n)
    # Space Complexity : O(n)

    def trap(self, height: List[int]) -> int:

        n = len(height)

        # Max height of the bar on the left side of the i'th bar
        maxLeftHeight = [0] * n 

        # Max height of the bar on the right side of the i'th bar
        maxRightHeight = [0] * n 

        # Calculating the max height of the bar on the left side of the i'th bar
        for i in range(1,n):
            maxLeftHeight[i] = max(height[i-1],maxLeftHeight[i-1])

        # Calculating the max height of the bar on the right side of the i'th bar
        for i in range(n-2,-1,-1):
            maxRightHeight[i] = max(height[i+1],maxRightHeight[i+1])

        totalAreaOfWater = 0 

        for i in range(n):

            maxHeightWaterCanReach = min(maxLeftHeight[i],maxRightHeight[i])

            if(height[i] < maxHeightWaterCanReach):
                totalAreaOfWater += maxHeightWaterCanReach - height[i]

        return totalAreaOfWater
            

    # Time Complexity : O(n)
    # Space Complexity : O(1)

    def trapWithTwoPointers(self, height: List[int]) -> int:

        n = len(height)

        maxLeftHeight = height[0]

        maxRightHeight = height[n-1]

        left = 1
        right = n-2 

        totalArea = 0 

        while left<=right:

            # Move towards the left side as water level would be dependent on the lesser height 
            if(maxLeftHeight < maxRightHeight):

                if(maxLeftHeight <= height[left]):
                    maxLeftHeight = height[left]

                else:
                    totalArea += maxLeftHeight - height[left]
                
                left += 1 

            # Move towards the right side 
            else:

                if(maxRightHeight <= height[right]):
                    maxRightHeight = height[right]

                else:
                    totalArea += maxRightHeight - height[right]

                right -= 1

        return totalArea


                

               


                

