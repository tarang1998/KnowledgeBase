from typing import List

class Solution:
    # Time Complexity: O(n) — We traverse the list once.
    # Space Complexity: O(n) — We use a separate result list.

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []  # This will store the resulting merged list of intervals

        for i in range(len(intervals)):
            # Case 1: newInterval is completely before the current interval
            # No overlap, and we can insert newInterval here and return the rest unchanged
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]  # Append the remaining intervals and return
            
            # Case 2: newInterval is completely after the current interval
            # No overlap, so just add the current interval to result
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # Case 3: Overlapping intervals
            # Merge the current interval with newInterval by taking min start and max end
            else:
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1])
                ]

        # If newInterval hasn’t been inserted yet, append it at the end
        res.append(newInterval)

        return res
