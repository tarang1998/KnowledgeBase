from typing import List

class Solution:

    def containsDuplicate(self,nums: List[int]) -> bool:
        # Time Complexity : O(n)
        # We use a set to keep track of numbers we've seen so far
        seen = set()

        for num in nums:
            # If the number is already in the set, it's a duplicate
            if num in seen:
                return True
            seen.add(num)  # Otherwise, add it to the set

        # If we finish the loop without finding duplicates
        return False

