
class Solution:

    def findMinDifference(self, timePoints: List[str]) -> int:

        bucket = [False]* 1440

        for timepoint in timePoints:

            timepoint = timepoint.split(":")

            hour = int(timepoint[0])
            minutes = int(timepoint[1])

            totalMinutes = (hour * 60) + minutes

            if(bucket[totalMinutes]):
                return 0
            
            bucket[totalMinutes] = True 

        
        curr = -1
        first = -1
        prev = - 1

        minMinutes = float('inf')

        for i in range(1440):
            if bucket[i] == True:
                curr = i 
                if first == -1:
                    first = curr

                if prev == -1:
                    prev = curr
                else: 
                    diff = curr-prev
                    if diff<minMinutes:
                        minMinutes = diff
                    prev = curr

        diff = 1440 - curr + first

        if diff<minMinutes:
            minMinutes = diff 
        
        return minMinutes



            
            








        