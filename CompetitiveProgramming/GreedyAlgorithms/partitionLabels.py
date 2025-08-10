class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        """
        Partitions the string into as many parts as possible
        so that each letter appears in at most one part.
        
        Time Complexity: O(n)
        Space Complexity: O(1) (extra space for 26 characters' last occurrence)
        """

        # Step 1: Store the last occurrence index of each character in s
        last_occurrence = {}
        for i, char in enumerate(s):
            last_occurrence[char] = i  # keep updating so we store the LAST occurrence

        # Step 2: Iterate through s to determine partition sizes
        partitions = []  # result list storing sizes of each partition
        start = 0  # start index of current partition
        end = 0    # farthest index this partition should reach

        for i, char in enumerate(s):
            # Update the farthest index we must reach for this partition
            end = max(end, last_occurrence[char])

            # If current index reaches the farthest point for this partition
            if i == end:
                # Partition size is end - start + 1
                partitions.append(end - start + 1)
                # Start a new partition
                start = i + 1

        return partitions