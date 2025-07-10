from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time Complexity : O(n)
        # Use a hash map to store {number: index}
        num_to_index = {}

        for i, num in enumerate(nums):
            # Calculate the complement that would sum up to the target
            complement = target - num

            # If the complement is already in the hash map, we found a solution
            if complement in num_to_index:
                return [num_to_index[complement], i]

            # Otherwise, store the current number with its index
            num_to_index[num] = i        


