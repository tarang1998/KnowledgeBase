from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        currSum = 0 
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        for num in nums:
            currSum += num
            #Value that needs to be subtracted from the current sum to get a value of k
            val = currSum - k 
            # Check if such a prefix is present 
            # Eg 1 -1 1 1 1 , currSum = 3, k = 3
            # Prefix sum(1 -1) is 0 
            # Possible subsets : 1 1 1, 1 -1 1 1 1  
            if val in prefixSum:
                res += prefixSum[val]
            prefixSum[currSum] += 1
        return res



  
                
    

        