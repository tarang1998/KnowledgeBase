class Solution:

    # Time Complexity : O(n)
    # Discard all the previous elements that result in a negative sum

    def maxSubArray(self, nums: List[int]) -> int:

        maxSum = nums[0]
        currSum = 0 

        for n in nums:
            # If the sum results to negative discard the calculated sum
            if(currSum < 0):
                currSum = 0 
            currSum += n
            # Keep capturing the maxSum regularly
            maxSum = max(maxSum,currSum)
        return maxSum


    def maxSubArray1(self, nums: List[int]) -> int:
        result = nums[0]
        currentSum = nums[0]

        for i in range(1,len(nums)):
            currentSum = max(nums[i], nums[i]+currentSum)
            result = max(currentMax,result)

        return result

        

        








