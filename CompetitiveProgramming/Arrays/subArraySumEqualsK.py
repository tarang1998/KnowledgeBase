from collections import defaultdict
from typing import List


class Solution:
   
    def subarraySum(self,nums: List[int], k: int) -> int:
        # Initialize variables
        count = 0               # Number of subarrays that sum to k
        curr_sum = 0            # Current prefix sum
        prefix_sums = defaultdict(int)  # Map to store frequencies of prefix sums
        prefix_sums[0] = 1      # Base case: a subarray that starts at index 0

        for num in nums:
            curr_sum += num  # Update the current prefix sum

            # If (curr_sum - k) exists in the map, it means there's a subarray ending here with sum = k
            count += prefix_sums[curr_sum - k]

            # Update the map with the current prefix sum
            prefix_sums[curr_sum] += 1

        return count



  
                
    

        