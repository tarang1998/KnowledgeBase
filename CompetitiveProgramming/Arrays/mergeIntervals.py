class Solution:

    # Time Complexity : O(n)
    # Space Complexity : O(1)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Sort the intervals according to the starting index
        intervals = sorted(intervals, key = lambda x:x[0])

        res = []

        intervalStartPointer = intervals[0][0]
        intervalEndPointer = intervals[0][1]

        for i in range(1,len(intervals)):

            nextStartPointer = intervals[i][0]
            nextEndPointer = intervals[i][1]

            # In this case the next interval overlaps with the previous interval
            if(nextStartPointer <=  intervalEndPointer ):

                # Merging the two intervals and assigning the new end pointer
                if(intervalEndPointer < nextEndPointer):
                    intervalEndPointer = nextEndPointer

            # In this case the intervals do not overlap with each other 
            # Add the previous interval in the result
            else:
                res.append([intervalStartPointer,intervalEndPointer])
                intervalStartPointer = nextStartPointer
                intervalEndPointer = nextEndPointer

        res.append([intervalStartPointer,intervalEndPointer])

        return res





        