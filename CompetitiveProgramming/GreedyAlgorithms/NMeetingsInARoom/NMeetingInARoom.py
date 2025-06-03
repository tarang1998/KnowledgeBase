#User function Template for python3

class Solution:
    

    def maximumMeetings(self,start,end):
        
        """
        Given two lists, start and end, of equal length n, where start[i] is the start time
        of meeting i and end[i] is the end time of meeting i, return the maximum number
        of non-overlapping meetings that can be scheduled in one room. A meeting that starts
        exactly when another ends is considered overlapping (i.e., we require start > previous end).
    
        Args:
            start (List[int]): list of start times.
            end (List[int]): list of end times.
    
        Returns:
            int: the maximum number of meetings.
        """
        n = len(start)
        if n == 0:
            return 0
    
        # Pair up each meeting's start and end time, then sort by end time ascending.
        meetings = sorted(zip(start, end), key=lambda x: x[1])
    
        count = 0
        last_end = -1  # Since all times are ≥ 0, initializing to -1 ensures the first meeting can be picked.
    
        for s, e in meetings:
            # We pick this meeting if its start is strictly greater than the last selected meeting's end.
            if s > last_end:
                count += 1
                last_end = e
    
        return count