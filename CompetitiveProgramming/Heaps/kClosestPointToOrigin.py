import heapq

class Solution:
    # O(nlogk)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        pq = []

        for point in points:

            x = point[0]
            y = point[1]

            dis = sqrt(pow(x,2) + pow(y,2))
            
            heapq.heappush(pq,(-dis,point))

            if len(pq) > k:
                heapq.heappop(pq)

        return  [ele[1] for ele in pq] 
        