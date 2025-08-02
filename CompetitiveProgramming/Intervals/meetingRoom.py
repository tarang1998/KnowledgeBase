class Solution:
    # Time Complexity: O(n log n) — because we sort the intervals
    # Space Complexity: O(1) — no extra space used (ignoring the sort)

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Step 1: Sort meetings by start time
        intervals.sort(key=lambda x: x[0])

        # Step 2: Check if any two meetings overlap
        for i in range(1, len(intervals)):
            # If the current meeting starts before the previous one ends — conflict!
            if intervals[i][0] < intervals[i-1][1]:
                return False  # Cannot attend both meetings

        # If we get here, all meetings are non-overlapping
        return True
