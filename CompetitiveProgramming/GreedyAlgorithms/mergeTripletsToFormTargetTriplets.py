from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Time Complexity : O(n)
        # We want to form a triplet exactly equal to target = [x, y, z]
        # The merging operation takes the max of each index
        # So we only care about triplets that are <= target in all positions
        # And we want to find at least one triplet with each component equal to target[i]

        # Initialize three flags to track whether we found the required values
        found = [False, False, False]  # found[i] means we've found a triplet with value target[i] at index i

        for triplet in triplets:
            # Skip any triplet that has a value greater than target in any position
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            # If a triplet matches target[i] in some position, mark it
            for i in range(3):
                if triplet[i] == target[i]:
                    found[i] = True

        # If all three positions are satisfied, return True
        return all(found)        