from typing import List


class Solution:

    def canJump(self, nums: List[int]) -> bool:
        # We use a greedy approach.
        # Time Complexity : O(n)
        # 'max_reach' represents the farthest index we can reach at any point.
        max_reach = 0

        for i in range(len(nums)):
            # If our current index is beyond the farthest reachable point,
            # it means we are stuck and can't proceed further.
            if i > max_reach:
                return False
            
            # Update max_reach with the farthest we can reach from current position
            max_reach = max(max_reach, i + nums[i])

            # If we can already reach or go beyond the last index, return True early
            if max_reach >= len(nums) - 1:
                return True

        # If loop completes, we have verified all positions are reachable
        return True

