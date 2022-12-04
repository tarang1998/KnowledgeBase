class Solution:

    # Time Complexity = O(n)
    # Space Complexity = O(1)
    def minimumAverageDifference(self, nums: List[int]) -> int:


        n = len(nums)

        #(O(n))
        totalSum = sum(nums)

        currentIndexPrefixSum = 0

        minAverageDifference = float('inf')
        minAverageDifferenceIndex = None

        #(O(n))
        for i in range(n):

            currentIndexPrefixSum += nums[i]

            avgFirstElements = currentIndexPrefixSum//(i+1)

            if(i == n-1):
                avgDiff = avgFirstElements
            else: 
                avgSecondElements = (totalSum - currentIndexPrefixSum)//(n-1-i)
                avgDiff = abs(avgFirstElements - avgSecondElements)


            if(minAverageDifference > avgDiff):
                minAverageDifference = avgDiff
                minAverageDifferenceIndex = i
                
        return minAverageDifferenceIndex





