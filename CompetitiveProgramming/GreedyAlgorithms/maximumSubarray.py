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









