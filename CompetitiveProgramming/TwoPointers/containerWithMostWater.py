class Solution:

    # Time Compexity : O(n)
    # Space Complexity : O(1)
    def maxArea(self, height: List[int]) -> int:

        l = 0 

        r = len(height) - 1

        maxArea = 0 

        while(l<r):

            h = min(height[l],height[r])

            area = h * (r-l)

            if(area > maxArea):
                maxArea = area 

            if(height[r]> height[l]):
                l+= 1

            elif(height[l] > height[r]):
                r-=1

            else:
                l+=1
                r-=1
        
        return maxArea