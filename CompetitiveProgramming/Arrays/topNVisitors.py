from collections import defaultdict
from datetime import datetime
import heapq

class Solution:

    def __init__(self):
        self.logs = []
        self.frequencyCount = defaultdict(int)
        self.consecutiveCount = {}
        self.consecutiveUsers = []


    def parse_logs(self, raw_data,start_time,end_time, consecutive_days):
        for data in raw_data:
            if start_time and start_time > date:
                continue
            if end_time and end_time < date:
                continue
            date, userId = data.split(", ")
            date = datetime.strptime(date, "%d-%b-%Y %I:%M %p")
            self.logs.append((date,userId))
            # Counting visit frequency
            self.frequencyCount[userId] += 1

            # Counting consecutive days
            if userId in self.consecutiveCount:
                count, prevLogDate = self.consecutiveCount[userId]
                delta = (date - prevLogDate)
                if delta.days >= 1 and delta.days < 2:
                    self.consecutiveCount[userId] = (count+1, date)
                else:
                    self.consecutiveCount[userId] = (1, date)
            else:
                self.consecutiveCount[userId] = (1,date)

            if self.consecutiveCount[userId][0] > consecutive_days:
                self.consecutiveUsers.append(userId)
            

    def findTopNCustomers(self,raw_data, k,consecutive_days):
        self.consecutiveUsers = []
        self.parse_logs(raw_data,None,None,consecutive_days)

        q = []
        for userId,count in self.frequencyCount.items():
            q.append((-count,userId))
        heapq.heapify(q)

        results = []
        for i in range(k):
            results.append(heapq.heappop(q)[1])

        print(results)



        








log = [
    "11-Jun-2018 1:00 AM, 1ABCDEFGHI",
    "11-Jun-2018 3:01 AM, 1ABCDEFGHI",
    "11-Jun-2018 4:12 AM, 2ABCDEFGHI",
    "12-Jun-2018 8:23 AM, 2ABCDEFGHI",
    "12-Jun-2018 4:21 AM, 3ABCDEFGHI",
    "13-Jun-2018 2:00 AM, 3ABCDEFGHI",
    "14-Jun-2018 10:00 PM, 3ABCDEFGHI"
]

sol = Solution()
customers = sol.findTopNCustomers(log,2,2)
