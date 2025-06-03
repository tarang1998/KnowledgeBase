"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:

    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        n = len(intervals)

        if n == 0:
            return 0 

        intervals = sorted(intervals, key = lambda x : x.end)

        minHeap = []

        maxRooms = 0 

        for interval in intervals:
            if minHeap and minHeap[0] <= interval.start:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, interval.end)
            maxRooms = max(maxRooms,len(minHeap))
        return maxRooms


    def minMeetingRooms1(self, intervals: List[Interval]) -> int:

        n = len(intervals)

        if n == 0:
            return 0 

        start = [interval.start for interval in intervals]
        end = [interval.end for interval in intervals]

        start = sorted(start)
        end = sorted(end)

        startPointer = 1 
        endPointer = 0


        maxResult = 1 
        count = 1 

        while startPointer <= n-1 and endPointer <= n-1:
            
            if (start[startPointer] < end[endPointer]):
                startPointer += 1
            else:
                endPointer += 1

            count = startPointer - endPointer
            maxResult = max(maxResult, count) 

        return maxResult
        
        