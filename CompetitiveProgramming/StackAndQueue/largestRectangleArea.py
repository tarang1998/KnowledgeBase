

class Solution:

    # Time Complexity : O(n)
    # Space Complexity : O(n)

    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea = 0 

        # Each stack element is a pair : (index,height)
        stack = []

        for index, height in enumerate(heights):

            start = index 

            while stack and stack[-1][1] > height:

                i,h = stack.pop()
                maxArea = max(maxArea, h * (index - i))
                start = i 


            stack.append((start,height))

        for index,height in stack:

            maxArea = max(maxArea , height * (len(heights) - index ))

        return maxArea 




        