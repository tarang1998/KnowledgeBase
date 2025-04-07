import heapq as hq
from collections import defaultdict

class Solution:

    # Bucket Sort
    # Time Complexity : O(n) 
    # Space Complexity : O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Calculate the frequency for each integer
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num,0)

        # Creating a freq array of size of nums
        # The index indicates the frequency of occurence 
        # and the value at the index is a list of elements that has that 
        # frequency of occurence 

        freq = [[] for i in range(len(nums)+1)]

        for key,value in count.items():
            freq[value].append(key)

        
        res = []
        for i in range(len(freq)-1,-1,-1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])

                if(len(res) == k):
                    return res





    # Time Complexity : O(klogn) 
    # Space Complexity : O(n+k)
    def topKFrequentUsingHeap(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:

            if num in count:
                count[num] += 1  
            else:
                count[num] = 1

        heap = [(-value, key) for key,value in count.items()]

        hq.heapify(heap)

        result = []

        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result


        





    # Time Complexity : O(nlogn)
    # Space Complexity : O(n)
    def topKFrequentSorting(self, nums: List[int], k: int) -> List[int]:

        count = defaultdict(int)

        for num in nums:

            count[num] += 1

        count = sorted(count.items(), key = lambda x:x[1], reverse = True)

        result = []

        for i in range(0,k):
            result.append(count[i][0]) 

        return result
        