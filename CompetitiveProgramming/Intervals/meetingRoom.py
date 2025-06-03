"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:

    # Time Complexity : O(nlogn)
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len(intervals) == 0:
            return True

        intervals = sorted(intervals, key = lambda x: x.start)

        startTime = intervals[0].start
        endTime = intervals[0].end

        for i in range(1,len(intervals)):

            if endTime > intervals[i].start:
                return False

            endTime = intervals[i].end

        return True