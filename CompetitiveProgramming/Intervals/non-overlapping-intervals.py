class Solution:
    # Time Complexity: O(n log n) because we sort the intervals by end time
    # Space Complexity: O(1) extra space (ignoring the input sort)

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Step 1: Sort the intervals by end time — greedy strategy
        intervals.sort(key=lambda x: x[1])
        
        # Count of non-overlapping intervals we can keep
        count = 0

        # The end of the last interval we kept
        prev_end = float('-inf')

        # Step 2: Iterate through the intervals
        for start, end in intervals:
            # If the current interval does not overlap with the last one
            if start >= prev_end:
                count += 1       # We can keep this interval
                prev_end = end   # Update the end to current's end
            # If it does overlap, we skip it (i.e., "remove" it)
            # We don't increase count, so it’s "removed"
        
        # Step 3: Return number of intervals to remove = total - kept
        return len(intervals) - count
