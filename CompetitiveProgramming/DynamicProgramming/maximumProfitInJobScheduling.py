
import bisect

class Solution:

    # Time Complexity : O(nlogn) : 
    # > Binary Search is called n times : n * log(n)
    # > Sorting of the jobs based on end time : nlogn

    # Space Complexity : O(n)
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        # Store each job in a tuple : [(endTime[i], startTime[i], profit[i])]
        jobs = zip(endTime,startTime,profit)

        # Sort the jobs according to their end Times 
        jobs = sorted(jobs)

        n = len(profit)

        # Initialize an array dp to record the profit obtained till the i'th job
        dp = [0] * (n+1)

        for i in range(n):

            startTime = jobs[i][1]
            profit = jobs[i][2]

            # To calculate the profit obtained till the ith job there are two scenarios
            # Calculate the profit including the ith job : need to find the latest job whose endTime does not overlap with the start time of the i'th job
            # Calculate the profit excluding the ith job
            # dp[i+1] = max(dp[i],dp[self.getLatestNonOverlappingJob(jobs,i,startTime)]+ profit)

            # Above operation can also be done by the bisect_right function to perform binary search to find
            # the latest job whose end time does not overlap with the current jobs start time 
            dp[i+1] = max(dp[i],dp[bisect.bisect_right(jobs, startTime, hi=i, key=lambda x: x[0])] + profit)

        return dp[n]

    # Perform binary search to find the latest non overlapping job
    def getLatestNonOverlappingJob(self,jobs,jobIndex,currentJobStartTime):

        low = 0 
        high = jobIndex

        while(low<high):

            mid = (low + high)//2

            endTime =jobs[mid][0]

            if(endTime <= currentJobStartTime):
                low = mid + 1
            else:
                high = mid
        
        return low 

        







        
    