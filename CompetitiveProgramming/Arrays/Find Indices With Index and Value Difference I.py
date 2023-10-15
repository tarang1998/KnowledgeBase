class Solution:

    # Brute Force Solution
    # Time Complexity : O(n^2)
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        
        for i in range(len(nums)):
            
            if(i + indexDifference < len(nums)):
            
                for j in range(i + indexDifference, len(nums)):
                                                    
                    if(abs(nums[i] - nums[j]) >=  valueDifference):
                        return [i, j]
                    
        return [-1,-1]
            
        
        