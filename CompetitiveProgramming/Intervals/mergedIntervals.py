class Solution:
    # Time Complexity: O(n log n) - we sort the intervals first
    # Space Complexity: O(n) - for storing the merged result
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals based on start time
        intervals.sort(key=lambda x: x[0])
        
        # This will hold our final merged intervals
        merged = []

        # Step 2: Go through each interval
        for interval in intervals:
            # If merged is empty OR there's no overlap with the last interval
            if not merged or merged[-1][1] < interval[0]:
                # Just add it — no overlap
                merged.append(interval)
            else:
                # There is an overlap — merge the current and last intervals
                merged[-1][1] = max(merged[-1][1], interval[1])
                # Example: [1,4] and [2,6] becomes [1,6]
        
        return merged
