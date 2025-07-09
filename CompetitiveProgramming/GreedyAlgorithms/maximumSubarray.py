from typing import List

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm     
        # Time Complexity : O(n)

        # Initialize two variables:
        # - current_sum to track the maximum subarray sum ending at the current position
        # - max_sum to track the overall maximum subarray sum found so far
        current_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # If current_sum + num is less than num itself,
            # it means starting a new subarray at num gives a better sum
            current_sum = max(num, current_sum + num)

            # Update max_sum if current_sum is greater than max_sum
            max_sum = max(max_sum, current_sum)

        return max_sum