import heapq

class Solution:

    #using Hashing 
    # Time Complexity : O(n)
    # Space Complexity : O(n)
    def longestConsecutiveWithHashing(self, nums: List[int]) -> int:


        hashTable = {}

        for num in nums:

            hashTable[num] = 1

        longestSequence = 0 

        for num in nums:


            #Check if num is the first element in its sequence 
            if(num-1 not in hashTable): # num is the first element

                val = num + 1
                while(val in hashTable):
                    val = val+1

                longestSequence = max(longestSequence,val - num)

        return longestSequence


    def longestConsecutive(self, nums: List[int]) -> int:

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








            



            
