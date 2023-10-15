class Solution:

    # Time Complexity : O(n)
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:


        minIndex = 0 
        maxIndex = 0 


        for i in range(indexDifference, len(nums)):

            # Finding minIndex and the maxIndex
            if(nums[i-indexDifference] < nums[minIndex]):
                minIndex = i-indexDifference

            if(nums[i-indexDifference] > nums[maxIndex]):
                maxIndex = i-indexDifference

            if(abs(minIndex - maxIndex)>= indexDifference and abs(nums[maxIndex] - nums[minIndex]) >= valueDifference):
                return [minIndex,maxIndex]
            
            # The difference between minIndex and maxIndex would always be greater than or equal to indexDifference
            if(abs(nums[maxIndex] - nums[i]) >= valueDifference):
                return [i,maxIndex]

            if(abs(nums[minIndex] - nums[i]) >= valueDifference):
                return [i,minIndex] 

        return [-1,-1]