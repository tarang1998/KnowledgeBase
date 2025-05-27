from collections import defaultdict, Counter
import heapq

class Solution:

    # Using a priority Queue
    # Time Complexity : O(klogn)
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        count = Counter(words)

        pq = []

        pq = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(pq)

        return [heapq.heappop(pq)[1] for _ in range(k)]


    

    # Time Complexity : O(nlogn)
    def topKFrequentUsingBucketSort(self, words: List[str], k: int) -> List[str]:

        count = defaultdict(int)

        for word in words:
            count[word] += 1 

        n = len(words)

        bucket = [[] for i in range(n+1)]
        
        for key,value in count.items():

            bucket[value].append(key)

    
        result = []

        for i in range(n,0,-1):

            if len(bucket[i]) == 1:
                result.append(bucket[i][0])
                if len(result) == k:
                    return result
            else:
                tmp = bucket[i]
                tmp = sorted(tmp)
                for t in tmp:
                    result.append(t)
                    if len(result) == k:
                        return result

                




        