import heapq

class Solution:

    # Time Complexity : O(n)
    # Space Complexity : O(n)
    def longestConsecutive(self, nums: List[int]) -> int:

        mem = set(nums)

        maxLength = 0 

        for num in mem:
            # Condition is true if num is the start of a certain sequence
            if num-1 not in mem:
                length = 1 
                while num + length in mem:
                    length += 1
                maxLength = max(maxLength, length)

        return maxLength


    def longestConsecutiveWithMinHeap(self, nums: List[int]) -> int:

        if(len(nums) == 0 ):
            return 0 

        priorityQueue = []

        #heapq by default implements a min heap

        for num in nums:

            heapq.heappush(priorityQueue,num)

        prev = heapq.heappop(priorityQueue)

        #Setting the initial count
        count = 1

        #Value for the longest consecutive subsequence
        max = 1

        while(len(priorityQueue)):

            # If condition is satisfied sequence is broken
            # Start counting for a new sequence 
            if(priorityQueue[0] - prev > 1):

                count = 1 

                prev = heapq.heappop(priorityQueue)

            # Skip the element - same sequence
            elif (priorityQueue[0] - prev == 0 ):

                prev = heapq.heappop(priorityQueue)

            # Sequence continues - increase count 
            else :

                count += 1

                prev = heapq.heappop(priorityQueue)

            if(count > max):

                max = count 

        return max








            



            
