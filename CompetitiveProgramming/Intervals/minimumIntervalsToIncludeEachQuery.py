import heapq  # For the min-heap

class Solution:
    # Time Complexity : O(nlogn)
    # Space Complexity : O(n)
    def minInterval(self,intervals, queries):
        # Sort intervals by their start (lefti)
        intervals.sort()
        
        # Store queries along with their original index so we can return answers in order
        indexed_queries = sorted((q, i) for i, q in enumerate(queries))
        
        result = [0] * len(queries)  # This will hold the final answers
        min_heap = []  # Heap to store (interval size, end point)
        i = 0  # Pointer for intervals
        
        # Loop through each query in increasing order
        for query, idx in indexed_queries:
            # Step 1: Push all intervals that start <= query into the heap
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                size = end - start + 1
                heapq.heappush(min_heap, (size, end))  # Push (size, right)
                i += 1
            
            # Step 2: Pop intervals from heap that end < query (cannot contain the query)
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            
            # Step 3: The top of the heap (if any) is the smallest valid interval
            if min_heap:
                result[idx] = min_heap[0][0]  # Get the size of the smallest interval
            else:
                result[idx] = -1  # No interval contains the query

        return result
