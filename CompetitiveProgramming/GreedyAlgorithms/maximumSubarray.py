class Solution:

    # Time Complexity : O(n)
    # Discard all the previous elements that result in a negative sum

    def maxSubArray(self, nums: List[int]) -> int:

        maxSum = nums[0]

        currSum = 0 

        for n in nums:

            # If the sum results to negative discard the caluculates sum
            if(currSum < 0):
                currSum = 0 

            currSum += n

            # Keep capturing the maxSum regularly
            maxSum = max(maxSum,currSum)

        return maxSum


    def maxSubArray1(self, nums: List[int]) -> int:

        maxValue = nums[0]
        maxValueTillNow = nums[0]

        for i in range(1,len(nums)):
            maxValueTillNow = max(nums[i], nums[i] + maxValueTillNow)
            if maxValueTillNow>maxValue:
                maxValue = maxValueTillNow 


        return maxValue

        

        








