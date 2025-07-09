from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # Time Complexity : O(n)
        # Initialize variables:
        # jumps: number of jumps made so far
        # current_end: farthest index we can reach with current number of jumps
        # farthest: farthest index we can reach in the current iteration
        jumps = 0
        current_end = 0
        farthest = 0

        # We iterate up to the second-last element because we don't need to jump *from* the last index
        for i in range(len(nums) - 1):
            # Update the farthest we can reach from index i
            farthest = max(farthest, i + nums[i])

            # If we have reached the end of the current jump's range,
            # we must make another jump to continue
            if i == current_end:
                jumps += 1
                current_end = farthest  # Move to the new farthest boundary

                # Optional early exit if we've already reached the end
                if current_end >= len(nums) - 1:
                    break

        return jumps

