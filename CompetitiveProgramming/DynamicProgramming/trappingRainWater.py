class Solution:

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
            


                

